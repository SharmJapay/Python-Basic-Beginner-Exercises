"""Solution for String Slicing and Substring Removal"""

from input_validation import (
    get_text,
    get_index,
    get_position,
    remove_chars,
    confirm_exit,
)


def main() -> None:
    """Starts the program ang executes the application flow"""

    while True:
        text = get_text()
        index = get_index()

        if index >= len(text):
            print(
                "The length of text must be greater than index. Removal of chars will not proceed."
            )
            print(f"The final text is '{text}'\n")

        else:
            position = get_position()
            sanitized_text = remove_chars(text, index, position)
            print(f"The new text is '{sanitized_text}'\n")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
