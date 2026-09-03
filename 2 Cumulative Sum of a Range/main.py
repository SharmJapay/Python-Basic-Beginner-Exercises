"""Solution for Cumulative Sum of a Range Exercise"""

from input_validation import input_number, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        prev_number = 0
        range_number = input_number()

        print("Printing current and previous number sum in a range(10)")

        for number in range(range_number):
            print(
                f"Current Number {number} Previous Number {prev_number} Sum: {number + prev_number}"
            )

            prev_number = number

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
