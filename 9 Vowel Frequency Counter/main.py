"""Solution for Vowel Frequency Counter Exercise"""

from input_validation import input_text, confirm_exit


def count_vowels(text: str) -> int:
    """Returns the number of vowel occurences in a string

    Arguments
        text [str]: The string that will be calculated

    Returns
        [int]: The number of vowel occurences in a string
    """

    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    total_count = 0

    for vowel in vowels.keys():
        vowel_count = 0

        for char in text.lower():
            if char == vowel:
                vowel_count += 1
                total_count += 1

        vowels[vowel] = vowel_count

    print(f"List of vowels and their counts: {vowels}")

    return total_count


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        text = input_text()
        number_of_vowels = count_vowels(text)

        print(f"\nThe number of vowels in the string '{text}' is '{number_of_vowels}'")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
