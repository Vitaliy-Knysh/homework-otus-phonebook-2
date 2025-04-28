import pytest
import argparse
from app.controller import parse_arguments

import app.controller


def test_parse_arguments(monkeypatch):
    # args_input = mock_input(argparse.Namespace(op_type='add', new_contact="{'wrong': wrong}", keyword=None))
    def mockinput():
        return 'smsmsmsmmsmsms'
    monkeypatch.setattr('builtins.input', mockinput)

    args_input = input()
    pass
