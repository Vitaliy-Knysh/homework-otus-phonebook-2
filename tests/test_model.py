import os

from app.model import Contact, Phonebook


def test_contact(valid_phone_numbers):
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
    def test_add_contact(dummy_contacts, setup_teardown_file):
        pb = Phonebook()
        for contact in dummy_contacts:
            pb.add_contact(contact)
        assert pb.get_all_contacts() == dummy_contacts

    @staticmethod
    def test_delete_contact(dummy_contacts, setup_teardown_file):
        pb = Phonebook()
        for contact in dummy_contacts:
            pb.add_contact(contact)
        pb.delete_contact('81112223344')
        assert pb.get_all_contacts() == list(dummy_contacts[1])
