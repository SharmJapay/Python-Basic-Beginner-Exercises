"""Solution for Removing Duplicates from a List Exercise"""

from input_validation import confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    data = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"\nData List: {data}")

    while True:
        sanitized_list = list(set(data))

        print(f"\nUnique List: {sanitized_list}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
