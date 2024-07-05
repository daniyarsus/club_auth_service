from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from phonenumbers import parse


class ResetPasswordWithEmailGetCodeDTO(BaseModel):
    email: EmailStr


class ResetPasswordWithEmailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str
    new_password: str

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')


class ResetPasswordWithPhoneGetCodeDTO(BaseModel):
    phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')


class ResetPasswordWithPhoneSetCodeDTO(BaseModel):
    phone: str
    code: str
    new_password: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')
