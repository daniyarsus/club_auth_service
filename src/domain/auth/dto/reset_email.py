from pydantic import BaseModel, EmailStr, field_validator, ValidationError


class ResetEmailGetCodeDTO(BaseModel):
    email: EmailStr


class ResetEmailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')
