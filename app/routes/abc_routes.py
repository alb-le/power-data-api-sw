from fastapi import APIRouter

from app.controllers.abc_controller import ControllerInterface

def add_crud_endpoints_to_router(router: APIRouter, controller: ControllerInterface) -> APIRouter:
    root_path = controller.path
    entity_type = controller.entity

    @router.post(f"/{root_path}")
    def create(entity: entity_type):
        return controller.create(entity)

    @router.get(f"/{root_path}/{{_id}}")
    def read(_id: str) -> entity_type:
        return controller.read(_id)

    @router.get(f"/{root_path}")
    def read_all() -> list[entity_type]:
        return controller.read_all()

    @router.put(f"/{root_path}/{{id_}}")
    def update(id_: str, entity: entity_type):
        return controller.update(id_, entity)

    @router.delete(f"/{root_path}/{{id_}}")
    def remove(id_: str):
        return controller.delete(id_)

    return router
