from pydantic import BaseModel, Field
from typing import List

class Event(BaseModel):
    name: str = Field(description="name of event if not available should make NA")
    link: str = Field(description="link of event if not available should make NA")
    type: str = Field(description="type of event maybe (work offre or emploi, training period , annoucement , event forum, other) if available if not should make NA")
    location: str = Field(description="location of event if not available should make NA")
    begin_date: str = Field(description="begin date  of event if not available should make NA")
    end_date: str = Field(description="end date  of event if not available should make NA")

class ScrapedEvents(BaseModel):
    events: List[Event] = Field(description="list of all event if available if not should make []")