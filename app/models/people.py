from pydantic import BaseModel

from app.models.types import datetime_iso


class People(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: list[str]
    species: list[str]
    vehicles: list[str]
    starships: list[str]
    created: datetime_iso
    edited: datetime_iso
    url: str
