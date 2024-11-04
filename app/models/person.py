from pydantic import BaseModel

from app.models.types import datetime_iso, Gender, Colors


class Person(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: Colors
    skin_color: Colors
    eye_color: Colors
    birth_year: str
    gender: Gender
    homeworld: str
    films: list[str]
    species: list[str]
    vehicles: list[str]
    starships: list[str]
    created: datetime_iso
    edited: datetime_iso
    url: str
