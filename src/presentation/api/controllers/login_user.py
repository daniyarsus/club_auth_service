from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from src.domain.auth.interfaces import LoginUserInterface
from src.domain.auth.dto import (
    LoginUserWithUsernameDTO,
    LoginUserWithEmailDTO,
    LoginUserWithPhoneDTO
)
from src.presentation.api.di import injector

router = APIRouter(prefix="/api/v1/auth/login", tags=["Login API endpoints."])


@router.post("/authenticate-username")
async def login_user(dto: OAuth2PasswordRequestForm = Depends()):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_username(dto=dto)
    return result


@router.post("/authenticate-email")
async def login_user(dto: LoginUserWithEmailDTO):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_email(dto=dto)
    return result


@router.post("/authenticate-phone")
async def login_user(dto: LoginUserWithPhoneDTO):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_phone(dto=dto)
    return result

