from fastapi import APIRouter

from .login_user import login_user_router
from .register_user import register_user_router


def setup_controllers(router: APIRouter):
    router.include_router(register_user_router)
    router.include_router(login_user_router)
