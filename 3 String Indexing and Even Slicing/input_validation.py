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
            text = input("Enter string here: ")

            if text and text.split():
                return text

            raise ValueError

        except ValueError:
            print("Error! Cannot accept empty input value. Try Again.")
            continue


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
