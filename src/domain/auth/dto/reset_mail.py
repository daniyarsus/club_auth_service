from pydantic import BaseModel, EmailStr, field_validator, ValidationError


class ResetMailGetCodeDTO(BaseModel):
    email: EmailStr
    old_password: str


class ResetMailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str
    new_password: str

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')
