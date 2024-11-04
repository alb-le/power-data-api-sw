from pydantic import BaseModel


class Starship(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: int
    length: int
    max_atmosphering_speed: int
    crew: str
    passengers: int
    cargo_capacity: int
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: list[str]
    films: list[str]
    created: str
    edited: str
    url: str
