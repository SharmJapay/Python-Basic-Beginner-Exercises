"""Solution for Word Frequency Counter (The Histogram) Exercise"""

from input_validation import input_text, confirm_exit


def word_counter(text: str, state="normal") -> dict:
    """Returns a dictionary that contains words (key) and the word count (value)

    Arguments
        text [str]: A string  that will be processed and counted

    Returns
        [dict]: A dictionary that contains words (key) and the word count (value)
    """

    dictionary = {}

    words = (
        [word.strip() for word in text.split(" ") if word]
        if state == "case_sensitive"
        else [word.strip().lower() for word in text.split(" ") if word]
    )

    for base_term in words:
        word_count = 0

        for word in words:
            if base_term == word:
                word_count += 1

        dictionary[base_term] = word_count

    return dictionary


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        text = input_text()
        counter = word_counter(text, "case_sensitive")
        print(f"\nWord Frequency Counter: \n{counter}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
