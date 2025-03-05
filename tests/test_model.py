from app.model import Contact, Phonebook
import os

from tests.conftest import setup_teardown_file


def test_contact(valid_phone_numbers, setup_teardown_file):
    for number in valid_phone_numbers:
        Contact(
            phone_number=number,
            name='name',
        )


class TestPhonebook:
    @staticmethod
    def test_phonebook_exists(setup_teardown_file):
        pb_exists = os.path.exists('phonebook.json')
        assert pb_exists

    @staticmethod
    def test_get_empty_contact_list(setup_teardown_file):
        contacts = Phonebook.get_all_contacts()
        assert contacts == []

    @staticmethod
    def test_add_contact(setup_teardown_file):
        pass

    @staticmethod
    def test_remove_contact(setup_teardown_file):
        pass

    @staticmethod
    def test_get_contact_list(setup_teardown_file):
        pb = Phonebook()
        for contact in dummy_contacts:
            pb.add_contact(contact)
        assert pb.get_all_contacts() == dummy_contacts
