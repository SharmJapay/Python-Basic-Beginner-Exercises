"""Solution for Custom Exponentiation Function Exercise"""

from input_validation import input_number, confirm_exit


def exponent(base: int, exp: int) -> int:
    """Returns an integer value of the base raised to the power of the exponent.

    Arguments
        base [int]: The base number
        exp [int]: The exponent number

    Returns
        [int] - The integer value of the base raised to the power of the exponent
    """

    result = base

    for _ in range(2, exp + 1):
        result *= base

    return result


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        base = input_number("base")
        exp = input_number("exponent")

        if base and exp:
            result = exponent(base, exp)
            print(f"\nThe result is {result}")

        else:
            print("Something error occured while doing operation")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
