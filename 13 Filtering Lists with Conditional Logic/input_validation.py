"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_number_list() -> list:
    """Returns a list of numbers

    Returns
        [list]: List of numbers
    """

    while True:
        try:
            input_numbers = input(
                "\nEnter a list of integer numbers here (separated by comma) (e.g  1, 2, 3, 4, 5): "
            )

            if not input_numbers:
                raise ValueError

            try:
                return [int(item) for item in input_numbers.split(",")]

            except ValueError:
                print(
                    "Error! Cannot accept other values except integers only. Try Again."
                )
                continue

        except ValueError:
            print("Error! Cannot accept empty input value. Try Again.")


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
