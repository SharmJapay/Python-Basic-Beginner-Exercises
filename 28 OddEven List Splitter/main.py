"""Solution for OddEven List Splitter Exercise"""

from input_validation import input_number_list, confirm_exit


def split_even(numbers: list) -> dict:
    """Returns a list that contains even numbers only

    Arguments
        numbers [list]: The base list of numbers

    Returns
        [list]: A list that contains even numbers only
    """

    return [number for number in numbers if number % 2 == 0]


def split_odd(numbers: list) -> dict:
    """Returns a list that contains odd numbers only

    Arguments
        numbers [list]: The base list of numbers

    Returns
        [list]: A list that contains odd numbers only
    """

    return [number for number in numbers if number % 2 == 1]


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        numbers = input_number_list()
        print(f"\nNumber List: {numbers}")

        even_list = split_even(numbers)

        print("\nEven numbers:")
        print(even_list)

        odd_list = split_odd(numbers)

        print("\nOdd numbers:")
        print(odd_list)

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
