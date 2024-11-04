from pydantic import BaseModel


class Vehicle(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: int
    length: float
    max_atmosphering_speed: int
    crew: int
    passengers: int
    cargo_capacity: int
    consumables: str
    vehicle_class: str
    pilots: list[str]
    films: list[str]
    created: str
    edited: str
    url: str
