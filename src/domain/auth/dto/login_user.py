from pydantic import BaseModel, EmailStr, validator
from phonenumbers import parse


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
