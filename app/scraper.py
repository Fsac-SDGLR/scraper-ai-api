import re
from scrapegraphai.graphs import SmartScraperGraph
from langchain_groq.chat_models import ChatGroq
from pydantic import BaseModel, Field
from typing import List
from langchain.output_parsers import OutputFixingParser, PydanticOutputParser
from langchain_core.exceptions import OutputParserException

MAX_TOKEN = 5500

class Event(BaseModel):
    name: str = Field(description="name of event if not available should make NA")
    link: str = Field(description="link of event if not available should make NA")
    type: str = Field(description="type of event maybe (work offre or emploi, training period , annoucement , event forum, other) if available if not should make NA")
    location: str = Field(description="location of event if not available should make NA")
    begin_date: str = Field(description="begin date  of event if not available should make NA")
    end_date: str = Field(description="end date  of event if not available should make NA")

class ScrapedEvents(BaseModel):
    events: List[Event] = Field(description="list of all event if available if not should make []")

graph_config = {
    "llm": {
        "model": "groq/deepseek-r1-distill-llama-70b",
        "api_key": "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",
        "temperature": 0,
        "model_tokens": MAX_TOKEN,
        "max_tokens": MAX_TOKEN
    },
    "headless": True,
    "verbose": False,
}

def scrape_events(website, user_prompt, keywords):
    
    ai_prompt = """
    You are an advanced web scraper and data extractor proficient in English, French, and Arabic. The user will provide a detailed request with a specific prompt, keywords, and a target website.

    Your task:
    1. Understand the context of the provided prompt, considering multilingual data (English, French, and Arabic).
    2. Focus on the provided keywords to identify relevant data across the supported languages.
    3. Scrape the target website as specified.
    4. Return the output in a structured JSON format with all relevant information extracted.

    Input:
    - Prompt: {user_prompt}
    - Keywords: {keywords}
    - Website: {website}

    Output:
    - Ensure accuracy, relevance, and inclusivity for the input parameters in all supported languages.
    - Provide a multilingual output where applicable, maintaining the integrity of data in English, French, and Arabic.
    - If no URL is available, set the value of the 'link' key to None.
    - Provide only the JSON output directly, without any surrounding text or introduction like 'Here is the JSON output:'
    - If a link is invalid or incomplete, correct it using this base path: {website}.

    Respond with the extracted data ready for further processing or analysis.
    """

    smart_scraper_graph = SmartScraperGraph(
        prompt=(ai_prompt),
        source=website,
        config=graph_config,
        schema=ScrapedEvents,
    )
    llm: ChatGroq = smart_scraper_graph.llm_model
    llm.model_kwargs['max_tokens'] = MAX_TOKEN
    del llm.model_kwargs['model_tokens']

    llm.with_structured_output(schema=ScrapedEvents, method='json_mode', include_raw=True)
    result = ""
    try:
        result = smart_scraper_graph.run()
    except OutputParserException as e:
        new_parser = OutputFixingParser.from_llm(parser=PydanticOutputParser(pydantic_object=ScrapedEvents), llm=llm)
        output = re.sub(r"<think>.*?</think>\n?", "", e.llm_output, flags=re.DOTALL)
        result = new_parser.parse(output)

    if result == "":
        return {"events": []}
    else:
        return result