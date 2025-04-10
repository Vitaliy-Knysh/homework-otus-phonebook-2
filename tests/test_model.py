import os

from app.model import Contact, Phonebook, ParsedArgs


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
        assert pb.delete_contact(dummy_contacts[0].phone_number)
        assert not pb.delete_contact('invalid_number')
        assert pb.get_all_contacts() == [dummy_contacts[1]]

    @staticmethod
    def test_search_contacts(dummy_contacts, setup_teardown_file):
        pb = Phonebook()
        for contact in dummy_contacts:
            pb.add_contact(contact)
        phone_number_search = pb.search_contacts(dummy_contacts[0].phone_number)
        keyword_search = pb.search_contacts('name')
        false_search = pb.search_contacts('false')
        assert phone_number_search == [dummy_contacts[0]]
        assert keyword_search == dummy_contacts
        assert false_search == []


def test_parsed_args():
    ParsedArgs(
        op_type='add',
        new_contact={'name': 'name2', 'phone_number': '+71112223344', 'comment': 'comment2'},
        keyword=''
    )
