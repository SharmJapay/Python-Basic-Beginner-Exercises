"""Solution for String Indexing and Even Slicing"""

from input_validation import get_text, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow"""

    while True:
        text = get_text()
        even_chars = text[0::2]

        print(f"Original String is '{text}'")
        print("Printing only even index chars")

        for char in even_chars:
            print(char)

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
