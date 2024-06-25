from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from phonenumbers import parse


class RegisterUserWithMailDTO(BaseModel):
    email: EmailStr
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) <= 3:
            raise ValidationError('Username must be at least 1 character!')


class RegisterUserWithMailGetCodeDTO(BaseModel):
    email: EmailStr


class RegisterUserWithMailSetCodeResponse(BaseModel):
    email: EmailStr
    code: str

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')


class RegisterUserWithPhoneDTO(BaseModel):
    phone: str
    username: str
    password: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) <= 3:
            raise ValidationError('Username must be at least 1 character!')

