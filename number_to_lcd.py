from constants import dictionary_of_display_formats


def number_to_lcd(number):
    outer_string = ""
    for digit in str(number):
        outer_string += dictionary_of_display_formats[int(digit)]
    return outer_string
