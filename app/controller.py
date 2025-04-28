import argparse
import json

from app.model import ParsedArgs, Contact


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='парсер аргументов для телефонной книги')
    parser.add_argument('--op_type', type=str, choices=['add', 'delete', 'change', 'search'],
                        help='add: добавить контакт\ndelete: удалить контакт\n'
                             'change: изменить контакт\nsearch: поиск контактов')
    parser.add_argument('--new_contact', type=json.loads, help='новый контакт для добавления')
    parser.add_argument('--keyword', type=str, help='ключевое слово для поиска')
    return parser


def parse_arguments(parser: argparse.ArgumentParser) -> ParsedArgs:
    """
    Преобразовывает объект-парсер в объект класса ParsedArgs
    """
    args = parser.parse_args()
    parsed_contact = args.new_contact
    new_contact = Contact(
        phone_number=parsed_contact['phone_number'],
        name=parsed_contact['name'],
        comment=parsed_contact['comment']

    )
    return ParsedArgs(
        op_type=args.op_type,
        new_contact=args.new_contact,
        keyword=args.keyword
    )


if __name__ == '__main__':
    parser = init_parser()
    a = parse_arguments(parser)
    print(a)
