from pydantic import BaseModel


class Specie(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: int
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: int
    homeworld: str
    language: str
    people: list[str]
    films: list[str]
    created: str
    edited: str
    url: str
