from fastapi import APIRouter

from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.dto import (
    RegisterUserWithEmailDTO,
    VerifyUserWithEmailGetCodeDTO,
    VerifyUserWithEmailSetCodeDTO
)
from src.presentation.api.di import injector

router = APIRouter(prefix="/api/v1/auth/register", tags=["Register API endpoints."])


@router.post("/create-email-user")
async def create_user_email_endpoint(dto: RegisterUserWithEmailDTO):
    register_user_service = await injector.get(RegisterUserInterface)
    return await register_user_service.register_user_with_email(
        dto=dto
    )


@router.post("/send-email-verify-code")
async def send_verify_email_code_endpoint(dto: VerifyUserWithEmailGetCodeDTO):
    register_user_service = await injector.get(RegisterUserInterface)
    return await register_user_service.get_email_code_verify_user(
        dto=dto
    )


@router.post("/send-email-verify-set-code")
async def get_verify_email_code_endpoint(dto: VerifyUserWithEmailSetCodeDTO):
    register_user_service = await injector.get(RegisterUserInterface)
    return await register_user_service.set_email_code_verify_user(
        dto=dto
    )
