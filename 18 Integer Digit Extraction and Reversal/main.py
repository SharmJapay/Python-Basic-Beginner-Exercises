"""Solution for Integer Digit Extraction and Reversal Exercise"""

from input_validation import input_number, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        number = input_number()

        while number > 0:
            digit = number % 10
            number = number // 10
            print(digit, end=" ")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
