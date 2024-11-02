from datetime import date

from pydantic import BaseModel

from app.models.types import datetime_iso


class Film(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: date
    characters: list[str]
    planets: list[str]
    starships: list[str]
    vehicles: list[str]
    species: list[str]
    created: datetime_iso
    edited: datetime_iso
    url: str
