from pydantic import BaseModel

class Planet(BaseModel):
    name: str
    rotation_period: int
    orbital_period: int
    diameter: int
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: list[str]
    films: list[str]
    url: str
