"""Solution for Check Palindrome Number Exercise"""

from input_validation import input_number, confirm_exit


def is_palindrome(number: int) -> bool:
    """Returns a boolean value after the number is validated as palindrome or not

    Arguments
        number [int]: The number checked if palindorme number or not

    Returns
        [bool] - The value after the number is validated as palindrome or not
    """

    reverse = ""
    original_number = number

    while number > 0:
        digit = number % 10
        number = number // 10
        reverse = reverse + str(digit)

    return original_number == int(reverse)


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        number = input_number()
        print(f"\nChecking if number {number} is palindrome...")

        palindrome_number = is_palindrome(number)

        if palindrome_number:
            print(f"\nYes! Given number {number} is a palindrome number")

        else:
            print(f"\nNo! Given number {number} is not a palindrome number")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
