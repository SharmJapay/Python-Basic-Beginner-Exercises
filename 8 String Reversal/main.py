"""Solution for String Reversal Exercise"""

from input_validation import input_text, confirm_exit


def reverse(text: str) -> str:
    """Returns the reverse value of the text

    Arguments
        text [str]: The inputted text

    Returns
        [str]: The reversed value of the string
    """

    return text[::-1]


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        text = input_text()
        print(f"\nYour inputted text is '{text}'")

        reversed_text = reverse(text)
        print(f"The reversed text is '{reversed_text}'\n")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
