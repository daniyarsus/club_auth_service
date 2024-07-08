from phonenumbers import parse
from pydantic import BaseModel, EmailStr, validator


class ResetPasswordWithEmailGetCodeDTO(BaseModel):
    email: EmailStr


class ResetPasswordWithEmailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str
    new_password: str

    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')


class ResetPasswordWithPhoneGetCodeDTO(BaseModel):
    phone: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')


class ResetPasswordWithPhoneSetCodeDTO(BaseModel):
    phone: str
    code: str
    new_password: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')

    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')
