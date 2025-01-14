from pydantic import BaseModel
from typing import List
from datetime import datetime

class Event(BaseModel):
    name: str
    link: str
    type: str
    location: str
    begin_date: str
    end_date: str

class ScrapedEvents(BaseModel):
    events: List[Event]