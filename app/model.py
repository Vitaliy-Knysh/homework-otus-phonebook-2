import re

from pydantic import BaseModel, field_validator


class Contact(BaseModel):
    phone_number: str
    name: str
    comment: str = None

    @classmethod
    @field_validator('phone_number')
    def validate_number(cls, value: str) -> str:
        phone_number_regex = r"[()\d+-]{11,}"
        if not re.fullmatch(pattern=phone_number_regex, string=value):
            raise ValueError(f"Неправильный номер телефона: {value}")
        return value


class Phonebook:

    @staticmethod
    def add_contact(contact: Contact):
        pass

    @staticmethod
    def delete_contact(phone_number: str):
        pass

    @staticmethod
    def change_contact():
        pass

    @staticmethod
    def get_all_contacts() -> list[Contact]:
        pass

    @staticmethod
    def search_contacts() -> list[Contact] | Contact:
        pass
