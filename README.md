# FastAPI Web AI Scraper

This is a FastAPI-based web ai scraper that extracts event information from a specified website using user-provided prompts and keywords. The scraper uses the `scrapegraphai` library and the Groq API for LLM-powered scraping.

## Features

- **Dynamic Inputs**: Users can provide the website URL, a prompt, and a list of keywords to scrape.
- **Structured Output**: The scraped data is returned in a structured JSON format.
- **Multilingual Support**: The scraper supports English, French, and Arabic content.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- scrapegraphai
- langchain-groq
- pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Fsac-SDGLR/scraper-ai-api.git
   cd fastapi-scraper
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:

   - Replace the `api_key` in `app/scraper.py` with your Groq API key.

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoint

### Scrape Events

- **Endpoint**: `POST /scrape/`
- **Description**: Scrapes events from a specified website based on the provided prompt and keywords.
- **Request Body**:

  ```json
  {
    "website": "https://ledesk.ma/encontinu/",
    "user_prompt": "Identifier tous les forums existants sur le site web",
    "keywords": ["forum", "discussion", "échange"]
  }
  ```

- **Response**:

  ```json
  {
    "events": [
      {
        "name": "Event Name",
        "link": "https://example.com/event",
        "type": "forum",
        "location": "Online",
        "begin_date": "2023-10-01",
        "end_date": "2023-10-02"
      }
    ]
  }
  ```

- **Example Request**:

  ```bash
  curl -X POST "http://127.0.0.1:8000/scrape/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "website": "https://ledesk.ma/encontinu/",
    "user_prompt": "Identifier tous les forums existants sur le site web",
    "keywords": ["forum", "discussion", "échange"]
  }'
  ```

---

## Project Structure

```
fastapi_scraper/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and endpoints
│   ├── models.py            # Pydantic models for data validation
│   ├── schemas.py           # API response schemas
│   └── scraper.py           # Scraping logic
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## Dependencies

The project uses the following libraries:

- **FastAPI**: For building the API.
- **Uvicorn**: For serving the FastAPI application.
- **scrapegraphai**: For web scraping.
- **langchain-groq**: For interacting with the Groq API.
- **pydantic**: For data validation and schema definitions.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [scrapegraphai](https://github.com/VinciGit00/Scrapegraph-ai) for the scraping framework.
- [Groq](https://groq.com/) for the LLM API.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.

---

This `README.md` provides a comprehensive guide to your project, making it easy for users and contributors to understand and use your FastAPI web scraper.