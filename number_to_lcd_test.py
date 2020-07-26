from constants import dictionary_of_display_formats
from number_to_lcd import number_to_lcd

import unittest

for _, v in dictionary_of_display_formats.items():
    print(v)


class NumberToLCDTestCase(unittest.TestCase):

    def test_displays_the_number_one_on_the_lcd(self):
        self.assertEqual(number_to_lcd(1), dictionary_of_display_formats[1])

    def test_displays_the_number_two_on_the_lcd(self):
        self.assertEqual(number_to_lcd(2), dictionary_of_display_formats[2])

    def test_displays_the_number_three_on_the_lcd(self):
        self.assertEqual(number_to_lcd(3), dictionary_of_display_formats[3])

    def test_displays_the_number_four_on_the_lcd(self):
        self.assertEqual(number_to_lcd(4), dictionary_of_display_formats[4])

    def test_displays_the_number_five_on_the_lcd(self):
        self.assertEqual(number_to_lcd(5), dictionary_of_display_formats[5])

    def test_displays_the_number_six_on_the_lcd(self):
        self.assertEqual(number_to_lcd(6), dictionary_of_display_formats[6])

    def test_displays_the_number_seven_on_the_lcd(self):
        self.assertEqual(number_to_lcd(7), dictionary_of_display_formats[7])

    def test_displays_the_number_eight_on_the_lcd(self):
        self.assertEqual(number_to_lcd(8), dictionary_of_display_formats[8])

    def test_displays_the_number_nine_on_the_lcd(self):
        self.assertEqual(number_to_lcd(9), dictionary_of_display_formats[9])

    def test_displays_the_number_zero_on_the_lcd(self):
        self.assertEqual(number_to_lcd(0), dictionary_of_display_formats[0])

    def test_displays_the_number_ten_on_the_lcd(self):
        self.assertEqual(number_to_lcd(10), dictionary_of_display_formats[1]+dictionary_of_display_formats[0])


if __name__ == '__main__':
    unittest.main()
