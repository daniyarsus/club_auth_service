from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from src.domain.auth.interfaces import LoginUserInterface
from src.domain.auth.dto import (
    LoginUserWithUsernameDTO,
    LoginUserWithEmailDTO,
    LoginUserWithPhoneDTO,
    GetRefreshTokenDTO
)
from src.presentation.api.di import injector

router = APIRouter(prefix="/api/v1/auth/login", tags=["Login API endpoints."])


@router.post("/username/authenticate")
async def authenticate_with_username_endpoint(form_data: OAuth2PasswordRequestForm = Depends()):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_username(dto=form_data)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )


@router.post("/email/authenticate")
async def authenticate_with_email_endpoint(dto: LoginUserWithEmailDTO):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_email(dto=dto)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )


@router.post("/phone/authenticate")
async def authenticate_with_phone_endpoint(dto: LoginUserWithPhoneDTO):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.authenticate_with_phone(dto=dto)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )


@router.post("/refresh_token")
async def get_refresh_token_endpoint(token: str):
    admin_auth_service = injector.get(LoginUserInterface)
    result = await admin_auth_service.get_refresh_token(token=token)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )
