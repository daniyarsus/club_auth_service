from pydantic import BaseModel, EmailStr, validator


class ResetEmailGetCodeDTO(BaseModel):
    email: EmailStr


class ResetEmailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str

    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')
