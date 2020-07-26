from constants import dictionary_of_display_formats
from number_to_lcd import number_to_lcd

import unittest


class NumberToLCDTestCase(unittest.TestCase):

    def test_displays_the_number_one_on_the_lcd(self):
        self.assertEqual(number_to_lcd(1), dictionary_of_display_formats[1])

    def test_displays_the_number_two_on_the_lcd(self):
        self.assertEqual(number_to_lcd(2), dictionary_of_display_formats[2])


if __name__ == '__main__':
    unittest.main()
