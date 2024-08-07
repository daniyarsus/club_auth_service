from phonenumbers import parse
from pydantic import BaseModel, EmailStr, validator


class LoginUserWithUsernameDTO(BaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, v):
        if len(v) <= 1:
            raise ValueError('Username must be at least 1 character!')


class LoginUserWithEmailDTO(BaseModel):
    email: EmailStr
    password: str


class LoginUserWithPhoneDTO(BaseModel):
    phone: str
    password: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')


class GetRefreshTokenDTO(BaseModel):
    token: str

    @validator('token')
    def validate_token(cls, v):
        if len(v) <= 1:
            raise ValueError('Token must be at least 1 character!')
