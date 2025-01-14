from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .scraper import scrape_events
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import sys


app = FastAPI()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (replace with specific origins in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define the request body schema
class ScrapeRequest(BaseModel):
    website: str
    user_prompt: str
    keywords: List[str]

# Define the response schema
class Event(BaseModel):
    name: str
    link: str
    type: str
    location: str
    begin_date: str
    end_date: str

class ScrapedEvents(BaseModel):
    events: List[Event]

@app.post("/scrape/", response_model=ScrapedEvents)
def scrape(request: ScrapeRequest):
    try:
        # Call the scrape_events function with user-provided inputs
        result = scrape_events(
            website=request.website,
            user_prompt=request.user_prompt,
            keywords=request.keywords
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)