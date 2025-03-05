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
    @setup_teardown_file()
    def test_phonebook_exists():
        pb_exists = os.path.exists('phonebook.json')
        assert pb_exists

    @setup_teardown_file
    def test_get_empty_contact_list(self):
        contacts = Phonebook.get_all_contacts()
        assert contacts == []

    @staticmethod
    def test_add_contact():
        pass

    @staticmethod
    def test_remove_contact():
        pass

    # def test_get_contact_list(self, dummy_contacts):
    #     for contact in dummy_contacts:
    #         self.pb.add_contact(contact)
    #     assert self.pb.get_all_contacts() == dummy_contacts
