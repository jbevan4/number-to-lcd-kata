from constants import dictionary_of_display_formats


def number_to_lcd_representation(number):
    return [dictionary_of_display_formats.get(number_to_look_up) for number_to_look_up in map(int, str(number))]


def print_number_from_representation(list_representation_of_number):
    for representation in zip(*list_representation_of_number):
        print(" ".join(representation))
