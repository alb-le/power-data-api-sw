from typing import Any

from fastapi import APIRouter
from mangum import Mangum


def create_crud_router(controller) -> Mangum:
    router = APIRouter()
    root_path = controller.root_path
    entity_type = controller.entity_type

    @router.post(f"{root_path}")
    def create(entity: entity_type):
        res = controller.create(entity)
        JSONResponse


    @router.get(f"/{root_path}")
    def get_all() -> entity_type:
        return {"router": "people"}

    @router.get(f"/{root_path}/{{_id}}")
    def get(_id) -> entity_type:
        return {"router": "people"}

    @router.post(f"/{root_path}")
    def pos

    return Mangum(router)


router_people = create_crud_router()
