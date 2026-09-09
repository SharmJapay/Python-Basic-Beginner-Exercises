"""
String Manipulation and Input Validation Utility Module.

This module provides a collection of robust, user-interactive functions designed
to safely collect validated inputs (strings, positive integers, and specific keyword choices)
from the console, alongside a core string-trimming utility function.
"""


def input_string_list() -> list:
    """Returns a list of strings

    Returns
        [list]: List of strings
    """

    while True:
        try:
            input_strings = input(
                "\nEnter a list here (separated by comma) (e.g  Apple, Banana, Cherry): "
            )

            if not input_strings:
                raise ValueError

            try:
                # return [int(item) for item in input_strings.split(",")]
                new_list = []

                for item in input_strings.split(","):
                    if not item.strip():
                        raise ValueError

                    new_list.append(item.strip().strip("\"'"))

                return new_list

            except ValueError:
                print("Error! Found an empty value item. Try Again.")
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
