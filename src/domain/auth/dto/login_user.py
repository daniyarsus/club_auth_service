from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from phonenumbers import parse


class LoginUserWithUsernameDTO(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) <= 1:
            raise ValueError('Username must be at least 1 character!')


class LoginUserWithMailDTO(BaseModel):
    email: EmailStr
    password: str


class LoginUserWithPhoneDTO(BaseModel):
    phone: str
    password: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')
