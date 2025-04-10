import pytest
import argparse
from app.controller import parse_arguments

import app.controller


def test_parse_arguments(mock_input, get_arguments):
    args_input = mock_input(argparse.Namespace(op_type='add', new_contact="{'wrong': wrong}", keyword=None))
    print(parse_arguments(args_input))
