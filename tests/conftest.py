import os
from argparse import Namespace

import pytest

from app.controller import parse_arguments
from app.model import Contact


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


@pytest.fixture()
def get_arguments():
    return [
        # ['--op_type', 'add', '--new_contact', "{'wrong': wrong}", '--keyword', 'None']
        Namespace(op_type='add', new_contact="{'wrong': wrong}", keyword=None),
        # Namespace(op_type='wrong',
        #           new_contact="{'name': 'name2', 'phone_number': '+71112223344', 'comment': 'comment2'}",
        #           keyword=''),
        # Namespace(op_type='add',
        #           new_contact="{'name': 'name2', 'phone_number': '+71112223344', 'comment': 'comment2'}",
        #           keyword=None),
        # Namespace(op_type='add',
        #           new_contact="{'name': 'name2', 'phone_number': '+71112223344', 'comment': 'comment2'}",
        #           keyword=None),
        # Namespace(op_type='delete',
        #           new_contact=None,
        #           keyword='wrong'),
        # Namespace(op_type='delete',
        #           new_contact=None,
        #           keyword='+71112223344'),
        # Namespace(op_type='change',
        #           new_contact=None,
        #           keyword='wrong')
    ]


# @pytest.fixture
# def mock_input(monkeypatch):
#     def mock(value):
#         monkeypatch.setattr('builtins.input', lambda _: 'value')
#     return mock


def test_args_input(mock_input):
    mock_input("--op_type=add --new_contact='{\"amogus\": \"sus\"}'")
    assert parse_arguments