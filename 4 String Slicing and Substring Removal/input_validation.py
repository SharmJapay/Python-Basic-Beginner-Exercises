"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def get_text() -> str:
    """Returns an input string

    Returns
        text [str]: The input string value
    """

    while True:
        try:
            text = input("Enter text here: ")

            if text and text.split():
                return text

            raise ValueError

        except ValueError:
            print("Error! Cannot accept empty input value. Try Again.")
            continue


def get_index() -> int:
    """Returns a positive integer value for the index number

    Returns
        number [int]: The index number value
    """

    while True:
        try:
            number = int(input("Enter index number: "))

            if number >= 0:
                return number

            raise ValueError

        except ValueError:
            print("Error! The input must be positive integer only. Try Again.")


def get_position() -> str:
    """Returns 'start' or 'end' string value

    Returns
        text [str]: The 'start' or 'end' string value
    """

    while True:
        try:
            answer = input("What position will be removed? (Type 'Start' or 'End'): ")

            if answer.lower() == "start" or answer.lower() == "end":
                return answer

            raise ValueError

        except ValueError:
            print("Error! Accepts 'Start' or 'End' values only. Try Again.")


def confirm_exit() -> str:
    """Returns 'yes' or 'no' string value

    Returns
        text [str]: The 'yes' or 'no' string value
    """

    while True:
        try:
            answer = input("Do you want to close the program? (Type 'Yes' or 'No'): ")

            if answer.lower() == "yes" or answer.lower() == "no":
                return answer

            raise ValueError

        except ValueError:
            print("Error! Accepts 'Yes' or 'No' values only. Try Again.")


def remove_chars(text: str, index: int, position: str) -> str:
    """Removes characters from text based on index given

    Arguments
        text [str]: The string value that will be sanitized
        index [int]: The last index for the removal of chars
        position [str]: The position where you want to start the removal of chars

    Returns
        [str]: The newly sanitized string value
    """

    if text and index >= 0 and position:
        if position == "start":
            return text[index:]

        elif position == "end":
            index = -index if index > 0 else None
            return text[:index]
