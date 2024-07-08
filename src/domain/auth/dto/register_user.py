from pydantic import BaseModel, EmailStr, validator, ValidationError
from phonenumbers import parse


class RegisterUserWithEmailDTO(BaseModel):
    email: EmailStr
    username: str
    password: str

    @validator('username')
    def validate_username(cls, v):
        if len(v) <= 3:
            raise ValueError('Username must be at least 4 characters long!')
        return v


class VerifyUserWithEmailGetCodeDTO(BaseModel):
    email: EmailStr


class VerifyUserWithEmailSetCodeDTO(BaseModel):
    email: EmailStr
    code: str

    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')
        return v


class RegisterUserWithPhoneDTO(BaseModel):
    phone: str
    username: str
    password: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')

    @validator('username')
    def validate_username(cls, v):
        if len(v) <= 3:
            raise ValueError('Username must be at least 1 character!')


class VerifyUserWithPhoneGetCodeDTO(BaseModel):
    phone: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')


class VerifyUserWithPhoneSetCodeDTO(BaseModel):
    phone: str
    code: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')
    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')
