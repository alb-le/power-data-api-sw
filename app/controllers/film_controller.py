from typing import Any

from app.controllers.abc_controller import ControllerInterface
from app.models.film import Film


class FilmController(ControllerInterface):
    path = '/film'
    entity = Film

    def create(self, film: Film) -> Film:
        pass

    def read(self, film_id: int) -> Film:
        film = Film(**self.swapi_service.get(f"{self.path}/{film_id}"))
        return film

    def update(self, film_id: int, film: Film) -> Film:
        pass

    def delete(self, id_: str):
        pass

film_controller = FilmController()