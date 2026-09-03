"""Solution for Finding Extremes (Min or Max) in a List Exercise"""

from input_validation import confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    numbers = [45, 2, 89, 12, 7]
    print(f"\nNumber List: {numbers}")

    while True:
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"\nLargest Number: {maximum}")
        print(f"Smallest Number: {minimum}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
