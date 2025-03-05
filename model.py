import re

from pydantic import BaseModel, field_validator


class Contact(BaseModel):
    phone_number: str
    name: str
    comment: str = None

    @field_validator('phone_number')
    def validate_number(cls, value: str) -> str:
        phone_number_regex = r"[()\d+-]{11,}"
        if not re.fullmatch(pattern=phone_number_regex, string=value):
            raise ValueError(f"Неправильный номер телефона: {value}")
        return value


class Phonebook:
    def __init__(self):
        contacts: list[Contact]


if __name__ == '__main__':
    print(re.match())
