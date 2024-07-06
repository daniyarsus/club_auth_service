from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

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
    try:
        register_user_service = injector.get(RegisterUserInterface)
        await register_user_service.register_user_with_email(dto=dto)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "User created successfully."}
        )
    except HTTPException as e:
        # Logging the exception for debugging
        print(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        # Logging any other exceptions
        print(f"Exception: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.post("/send-email-verify-code")
async def send_verify_email_code_endpoint(dto: VerifyUserWithEmailGetCodeDTO):
    register_user_service = injector.get(RegisterUserInterface)
    await register_user_service.get_email_code_verify_user(
        dto=dto
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Email verification code has been sent."}
    )


@router.post("/send-email-verify-set-code")
async def get_verify_email_code_endpoint(dto: VerifyUserWithEmailSetCodeDTO):
    register_user_service = injector.get(RegisterUserInterface)
    await register_user_service.set_email_code_verify_user(
        dto=dto
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Email has been verified successfully."}
    )
