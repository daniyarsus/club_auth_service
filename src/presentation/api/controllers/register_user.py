from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.dto import (
    RegisterUserWithEmailDTO,
    VerifyUserWithEmailGetCodeDTO,
    VerifyUserWithEmailSetCodeDTO
)
from src.presentation.api.di import injector


class RegisterUserRoutes:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1/auth/register", tags=["Register API endpoints"])
        self._routes()

    def _routes(self):
        @self.router.post("/email/add-user")
        async def create_user_email_endpoint(dto: RegisterUserWithEmailDTO):
            register_user_service = injector.get(RegisterUserInterface)
            await register_user_service.register_user_with_email(dto=dto)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "User created successfully."}
            )

        @self.router.post("/email/get-code")
        async def send_verify_email_code_endpoint(dto: VerifyUserWithEmailGetCodeDTO):
            register_user_service = injector.get(RegisterUserInterface)
            result = await register_user_service.get_email_code_verify_user(dto=dto)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": f"Email verification code has been sent. {result}"}
            )

        @self.router.post("/email/send-code")
        async def get_verify_email_code_endpoint(dto: VerifyUserWithEmailSetCodeDTO):
            register_user_service = injector.get(RegisterUserInterface)
            await register_user_service.set_email_code_verify_user(dto=dto)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "Email has been verified successfully."}
            )


register_user_router = RegisterUserRoutes().router
