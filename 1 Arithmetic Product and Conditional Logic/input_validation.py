"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_number(place: str) -> int | None:
    """Returns a valid integer value if input conditions are met, otherwise None

    Arguments
        place [str]: The value must be 'first' or 'second' only

    Returns
        number [int] or None
    """

    if place not in ["first", "second"]:
        print(f"Invalid argument value: '{place}'")
        return

    while True:
        try:
            number = int(input(f"Enter {place} number: "))

            if number > 0:
                return number

            raise ValueError

        except ValueError:
            print("Error! The number must be positive integer value only")


def confirm_exit() -> str:
    """Returns yes or no string value

    Returns
        text [str]: The yes or no string value
    """

    while True:
        try:
            answer = input("Do you want to close the program? (Type 'Yes' or 'No'): ")

            if answer.lower() == "yes" or answer.lower() == "no":
                return answer

            raise ValueError

        except ValueError:
            print("Error! Accepts 'Yes' or 'No' values only. Try Again.")
