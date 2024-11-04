from typing import Any

from app.controllers.abc_controller import ControllerInterface
from app.models.person import Person


class PersonController(ControllerInterface):
    path = '/film'
    entity = Person

    def create(self, person: Person) -> Person:
        pass

    def read(self, film_id: int) -> Person:
        film = Person(**self.swapi_service.get(f"{self.path}/{film_id}"))
        return film

    def update(self, film_id: int, film: Person) -> Person:
        pass

    def delete(self, id_: str):
        pass

person_controller = PersonController()