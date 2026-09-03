"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_item() -> str:
    """Returns an input item

    Returns
        text [str]: The input item value
    """

    while True:
        try:
            item = input("Enter item here: ")

            if item and item.split():
                return item

            raise ValueError

        except ValueError:
            print("Error! Cannot accept empty input value. Try Again.")
            continue


def input_index_number() -> int:
    """Returns a positive integer number value

    Returns
        number [int]: The index number value
    """

    while True:
        try:
            number = int(input("Enter list index number to remove: "))

            if number >= 0:
                return number

            raise ValueError

        except ValueError:
            print("Error! The input must be positive integer only. Try Again.")


def do_action() -> str:
    """Returns 'add' or 'remove' string value

    Returns
        text [str]: The 'add' or 'remove' string value
    """

    while True:
        try:
            answer = input(
                "\nWhat do you want to do with the list? (Type 'Add' or 'Remove'): "
            )

            if answer.lower() == "add" or answer.lower() == "remove":
                return answer

            raise ValueError

        except ValueError:
            print("Error! Accepts 'Add' or 'Remove' values only. Try Again.")


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
