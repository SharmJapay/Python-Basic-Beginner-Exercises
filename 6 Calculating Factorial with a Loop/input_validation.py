"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_number() -> int:
    """Returns a positive integer value

    Returns
        number [int]: The index number value
    """

    while True:
        try:
            number = int(input("\nEnter an integer number: "))

            if number >= 0:
                return number

            raise ValueError

        except ValueError:
            print("Error! The input must be positive integer only. Try Again.")


def confirm_exit() -> str:
    """Returns 'yes' or 'no' string value

    Returns
        text [str]: The 'yes' or 'no' string value
    """

    while True:
        try:
            answer = input("\nDo you want to close the program? (Type 'Yes' or 'No'): ")

            if answer.lower() == "yes" or answer.lower() == "no":
                return answer

            raise ValueError

        except ValueError:
            print("Error! Accepts 'Yes' or 'No' values only. Try Again.")
