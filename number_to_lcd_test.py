from constants import number_one_in_lcd_form
from number_to_lcd import number_to_lcd

import unittest


class NumberToLCDTestCase(unittest.TestCase):

    def test_displays_the_number_one_on_the_lcd(self):
        self.assertEqual(number_to_lcd(1), number_one_in_lcd_form)


if __name__ == '__main__':
    unittest.main()
