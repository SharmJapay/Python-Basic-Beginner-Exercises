"""Solution for Nested Loops for Multiplication Exercise"""

from input_validation import confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        for number1 in range(1, 11):
            for number2 in range(1, 11):
                print(f"{number1 * number2}", end=" ")

            print("\n")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
