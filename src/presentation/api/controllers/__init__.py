from fastapi import APIRouter

from .login_user import *
from .register_user import router as register_user_router


def setup_controllers(router: APIRouter):
    router.include_router(register_user_router)
