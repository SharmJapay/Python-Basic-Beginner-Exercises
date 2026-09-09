"""Solution for Word Length Analysis Exercise"""

from input_validation import input_string_list, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        strings = input_string_list()
        print(f"\nString List: \n{strings}")
        print("\nStrings and Character Count: ")

        for string in strings:
            print(f"{string} - {len(string)}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
