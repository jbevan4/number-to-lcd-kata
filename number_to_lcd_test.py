from contextlib import contextmanager
from io import StringIO
from number_to_lcd import number_to_lcd_representation
from number_to_lcd import print_number_from_representation

import sys
import unittest
import pytest


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


@pytest.mark.parametrize("test_input,expected",
                         [(1, " \n|\n|\n"), (2, "_ \n_|\n|_\n"), (3, "_ \n_|\n_|\n"),
                          (4, "   \n|_|\n  |\n"), (5, " _ \n|_ \n _|\n"), (6, "   \n|_ \n|_|\n"),
                          (7, "_ \n |\n |\n"), (8, " _ \n|_|\n|_|\n"), (9, " _\n|_|\n  |\n"),
                          (0, " _ \n| |\n|_|\n")])
def test_displays_single_digits_on_the_lcd(test_input, expected):
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(test_input))
        output = out.getvalue()
        assert output == expected


def test_displays_the_number_ten_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(10))
        output = out.getvalue()
        assert output == "   _ \n| | |\n| |_|\n"
