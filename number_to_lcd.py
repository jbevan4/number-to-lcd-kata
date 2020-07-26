from constants import dictionary_of_display_formats


def number_to_lcd(number):
    return dictionary_of_display_formats.get(number)