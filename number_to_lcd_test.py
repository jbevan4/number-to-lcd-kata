from number_to_lcd import number_to_lcd_representation
from number_to_lcd import print_number_from_representation

import pytest


@pytest.mark.parametrize("test_input,expected",
                         [(1, " \n|\n|\n"), (2, "_ \n_|\n|_\n"), (3, "_ \n_|\n_|\n"),
                          (4, "   \n|_|\n  |\n"), (5,
                                                   " _ \n|_ \n _|\n"), (6, "   \n|_ \n|_|\n"),
                          (7, "_ \n |\n |\n"), (8,
                                                " _ \n|_|\n|_|\n"), (9, " _\n|_|\n  |\n"),
                          (0, " _ \n| |\n|_|\n")])
def test_displays_single_digits_on_the_lcd(test_input, expected, capsys):
    print_number_from_representation(number_to_lcd_representation(test_input))
    captured = capsys.readouterr()
    with capsys.disabled():
        print(f"\n{captured.out}")
    assert captured.out == expected


def test_displays_the_number_ten_on_the_lcd(capsys):
    print_number_from_representation(number_to_lcd_representation(10))
    captured = capsys.readouterr()
    with capsys.disabled():
        print(f"\n{captured.out}")
    assert captured.out == "   _ \n| | |\n| |_|\n"


def test_displays_the_number_eleven_on_the_lcd(capsys):
    print_number_from_representation(number_to_lcd_representation(11))
    captured = capsys.readouterr()
    with capsys.disabled():
        print(f"\n{captured.out}")
    assert captured.out == "   \n| |\n| |\n"
