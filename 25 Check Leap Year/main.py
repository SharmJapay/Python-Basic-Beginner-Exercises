"""Solution for Check Leap Year Exercise"""

from input_validation import input_year, confirm_exit


def is_leap(year: int) -> bool:
    """Returns True or False if year is a leap year

    Arguments
        year [int]: The year number

    Returns
        [bool] - Boolean value if year is a leap year
    """

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    else:
        return False


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        year = input_year()

        print(f"\nYear: {year}")

        if is_leap(year):
            print(f"\n{year} is a leap year ")

        else:
            print(f"\n{year} is not a leap year ")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
