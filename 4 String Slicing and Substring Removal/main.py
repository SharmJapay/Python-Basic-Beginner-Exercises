"""Solution for String Slicing and Substring Removal Exercise"""

from input_validation import (
    input_text,
    input_index_number,
    input_position,
    remove_chars,
    confirm_exit,
)


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        text = input_text()
        index = input_index_number()

        if index >= len(text):
            print(
                "The length of text must be greater than index. Removal of chars will not proceed."
            )
            print(f"The final text is '{text}'\n")

        else:
            position = input_position()
            sanitized_text = remove_chars(text, index, position)
            print(f"The new text is '{sanitized_text}'\n")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
