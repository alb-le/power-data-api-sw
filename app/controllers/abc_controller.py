from abc import ABC
from typing import Any, ClassVar

from app.services.swapi import SwApiService


class ControllerInterface(ABC):
    path: ClassVar[str]
    entity: ClassVar[Any]
    swapi_service: SwApiService = SwApiService()

    def create(self, entity: Any) -> Any:
        raise NotImplementedError

    def read(self, id_: str) -> Any:
        raise NotImplementedError

    def read_all(self) -> list[Any]:
        raise NotImplementedError

    def update(self, id_: str, entity: Any) -> Any:
        raise NotImplementedError

    def delete(self, id_: str) -> str | None:
        raise NotImplementedError
