"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_year() -> int:
    """Returns a year number

    Returns
        year [int]: The year number
    """

    while True:
        try:
            year = int(input("\nEnter year: "))

            if year > 0:
                return year

            raise ValueError

        except ValueError:
            print("Error! The year must be greater than 0. Try Again.")


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
