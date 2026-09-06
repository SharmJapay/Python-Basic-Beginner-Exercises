"""Solution for Downward Half-Pyramid Pattern Exercise"""

from input_validation import input_number, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        rows = input_number()
        print(f"\nRows: {rows}\n")

        while rows > 0:
            for _ in range(1, rows + 1):
                print("*", end=" ")

            print("\n", end="")
            rows = rows - 1

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
