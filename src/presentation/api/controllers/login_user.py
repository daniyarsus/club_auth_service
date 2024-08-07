from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.domain.auth.dto import (GetRefreshTokenDTO, LoginUserWithEmailDTO,
                                 LoginUserWithPhoneDTO,
                                 LoginUserWithUsernameDTO)
from src.domain.auth.interfaces import LoginUserInterface
from src.presentation.api.di import injector


class LoginUserRoutes:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1/auth/login", tags=["Login API endpoints"])
        self._routes()

    def _routes(self):
        @self.router.post("/username/authenticate")
        async def authenticate_with_username_endpoint(form_data: OAuth2PasswordRequestForm = Depends()):
            login_user_service: LoginUserInterface = injector.get(LoginUserInterface)
            result = await login_user_service.authenticate_with_username(dto=form_data)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result
            )

        @self.router.post("/email/authenticate")
        async def authenticate_with_email_endpoint(dto: LoginUserWithEmailDTO):
            login_user_service: LoginUserInterface = injector.get(LoginUserInterface)
            result = await login_user_service.authenticate_with_email(dto=dto)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result
            )

        @self.router.post("/phone/authenticate")
        async def authenticate_with_phone_endpoint(dto: LoginUserWithPhoneDTO):
            login_user_service: LoginUserInterface = injector.get(LoginUserInterface)
            result = await login_user_service.authenticate_with_phone(dto=dto)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result
            )

        @self.router.post("/refresh_token")
        async def get_refresh_token_endpoint(token: str):
            login_user_service: LoginUserInterface = injector.get(LoginUserInterface)
            result = await login_user_service.get_refresh_token(token=token)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result
            )


login_user_router: LoginUserRoutes = LoginUserRoutes().router
