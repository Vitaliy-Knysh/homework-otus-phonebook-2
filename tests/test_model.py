from model import Contact


def test_contact(valid_phone_numbers):
    for number in valid_phone_numbers:
        Contact(
            phone_number=number,
            name='name',
            # comment='comment'
        )
