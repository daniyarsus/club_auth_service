from pydantic import BaseModel, field_validator, ValidationError
from phonenumbers import parse


class ResetPhoneGetCodeDTO(BaseModel):
    phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')


class ResetPhoneSetCodeDTO(BaseModel):
    phone: str
    code: str
    hew_phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not parse(v):
            raise ValidationError('Phone number must be entered in the format: +999999999!')

    @field_validator('code')
    def validate_code(cls, v):
        if len(v) != 6:
            raise ValidationError('Code must be 6 digits!')
