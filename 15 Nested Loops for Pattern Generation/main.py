"""Solution for Removing Duplicates from a List Exercise"""

from input_validation import input_number, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        number = input_number()
        print(f"\nNumber: {number}")

        for i in range(number + 1):
            text = ""

            for _ in range(i):
                text += " " + str(i)

            print(text)

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
