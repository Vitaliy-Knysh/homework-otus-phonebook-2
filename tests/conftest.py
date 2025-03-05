import pytest


@pytest.fixture()
def valid_phone_numbers():
    return (
        '81112223344',
        '+71112223344',
        '+7-111-222-33-44',
        '8-111-222-3344'
    )
