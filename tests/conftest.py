import os

import pytest

from app.model import Contact, Phonebook


@pytest.fixture()
def valid_phone_numbers():
    return (
        '81112223344',
        '+71112223344',
        '+7-111-222-33-44',
        '8-111-222-3344'
    )


@pytest.fixture()
def dummy_contacts():
    return [
        Contact(
            name='name1',
            phone_number='81112223344',
            comment=''
        ),
        Contact(
            name='name2',
            phone_number='+71112223344',
            comment='comment2'
        ),
    ]


@pytest.fixture()
def setup_teardown_file():
    if not os.path.exists('phonebook.json'):
        open("phonebook.json", "w").close()
    yield
    os.remove('phonebook.json')
