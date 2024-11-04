from fastapi import APIRouter

from app.controllers.film_controller import film_controller
from app.controllers.person_controller import person_controller
from app.routes.abc_routes import add_crud_endpoints_to_router

router = APIRouter()
controllers = [film_controller, person_controller]

for controller in controllers:
    add_crud_endpoints_to_router(router, controller)
