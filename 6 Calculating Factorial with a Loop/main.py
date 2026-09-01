"""Solution for Calculating Factorial with a Loop Exercise"""

from input_validation import get_number, confirm_exit


def factorial(number: int) -> int:
    """Returns the factorial of a number

    Arguments
        number [int]: The number used for factorial

    Returns
        [int] - The factorial result of a number
    """
    if number == 0:
        return 1

    return number * factorial(number - 1)


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        number = get_number()
        result_method1 = 1

        # Solution Method: Use of For Loop
        for i in range(1, number + 1):
            result_method1 = result_method1 * i

        print(f"The factorial of {number} using first method is {result_method1}")

        # Alternative Method: Use of user-defined function factorial()
        result_method2 = factorial(number)

        print(f"The factorial of {number} using second method is {result_method2}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
