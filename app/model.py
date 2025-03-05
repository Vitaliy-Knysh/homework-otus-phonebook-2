import json
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
        with open('phonebook.json') as file:
            contacts_dict = file.read()
            if contacts_dict:
                contacts_dict = json.loads(contacts_dict)
            else:
                contacts_dict = {}
        contacts_dict.setdefault(contact.phone_number, contact.model_dump())
        with open('phonebook.json', 'w') as file:
            file.write(json.dumps(contacts_dict))

    @staticmethod
    def delete_contact(phone_number: str) -> bool:
        with open('phonebook.json') as file:
            contacts_dict = file.read()
        if not contacts_dict:
            return False
        contacts_dict = json.loads(contacts_dict)
        if phone_number not in contacts_dict:
            return False
        contacts_dict.pop(phone_number)
        with open('phonebook.json', 'w') as file:
            file.write(json.dumps(contacts_dict))
        return True

    @staticmethod
    def change_contact(phone_number: str, new_contact: Contact):
        pass

    @staticmethod
    def get_all_contacts() -> list[Contact]:
        with open('phonebook.json') as file:
            contacts_dict = file.read()
            if contacts_dict:
                contacts_dict = json.loads(contacts_dict)
            else:
                return []
        contacts_list = []
        for contact in contacts_dict.values():
            contacts_list.append(Contact(
                phone_number=contact['phone_number'],
                name=contact['name'],
                comment=contact.get('comment')
            ))
        return contacts_list

    @staticmethod
    def search_contacts(search_value) -> list[Contact] | Contact:
        with open('phonebook.json') as file:
            contacts_dict = file.read()
            if contacts_dict:
                contacts_dict = json.loads(contacts_dict)
            else:
                return []
        return_contacts = []
        for contact in contacts_dict.values():
            if search_value in str(contact):
                return_contacts.append(
                    Contact(
                        phone_number=contact['phone_number'],
                        name=contact['name'],
                        comment=contact.get('comment')
                    )
                )
        return return_contacts
