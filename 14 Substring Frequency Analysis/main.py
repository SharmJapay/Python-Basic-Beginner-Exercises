"""Solution for String Reversal Exercise"""

from input_validation import input_text, confirm_exit


def count_words(sentence: str, substring: str) -> int:
    """Returns the number of word frequencey in a text

    Arguments
        sentence (str): The whole text where pattern matching will be done.
        substring (str): The string that will processed for pattern matching

    Returns
        [int]: The number of word frequencey in a text
    """

    return sentence.count(substring)


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        sentence = input_text()
        print(f"\nThe sentence string is '{sentence}'")

        substring = input_text()
        print(f"\nThe word for pattern matching '{substring}'")

        word_count = count_words(sentence, substring)
        print(f"\n'{substring}' appeared '{word_count}' times")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
