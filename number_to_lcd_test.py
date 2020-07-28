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


def test_displays_the_number_one_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(1))
        output = out.getvalue()
        assert output == " \n|\n|\n"


def test_displays_the_number_two_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(2))
        output = out.getvalue()
        assert output == "_ \n_|\n|_\n"


def test_displays_the_number_three_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(3))
        output = out.getvalue()
        assert output == "_ \n_|\n_|\n"


def test_displays_the_number_four_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(4))
        output = out.getvalue()
        assert output == "   \n|_|\n  |\n"


def test_displays_the_number_five_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(5))
        output = out.getvalue()
        assert output == " _ \n|_ \n _|\n"


def test_displays_the_number_six_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(6))
        output = out.getvalue()
        assert output == "   \n|_ \n|_|\n"


def test_displays_the_number_seven_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(7))
        output = out.getvalue()
        assert output == "_ \n |\n |\n"


def test_displays_the_number_eight_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(8))
        output = out.getvalue()
        assert output == " _ \n|_|\n|_|\n"


def test_displays_the_number_nine_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(9))
        output = out.getvalue()
        assert output == " _\n|_|\n  |\n"


def test_displays_the_number_zero_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(0))
        output = out.getvalue()
        assert output == " _ \n| |\n|_|\n"


def test_displays_the_number_ten_on_the_lcd():
    with captured_output() as (out, err):
        print_number_from_representation(number_to_lcd_representation(10))
        output = out.getvalue()
        assert output == "   _ \n| | |\n| |_|\n"


if __name__ == '__main__':
    unittest.main()
