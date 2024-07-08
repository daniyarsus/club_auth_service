from phonenumbers import parse
from pydantic import BaseModel, validator


class ResetPhoneGetCodeDTO(BaseModel):
    phone: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')


class ResetPhoneSetCodeDTO(BaseModel):
    phone: str
    code: str
    hew_phone: str

    @validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValueError('Phone number must be entered in the format: +999999999!')

    @validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValueError('Code must be 6 digits!')
