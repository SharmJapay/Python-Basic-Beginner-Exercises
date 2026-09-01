"""Solution for Cumulative Sum of a Range"""


def main() -> None:
    """Starts the program and executes the applications flow"""

    prev_number = 0

    print("Printing current and previous number sum in a range(10)")

    for number in range(10):
        print(
            f"Current Number {number} Previous Number {prev_number} Sum: {number + prev_number}"
        )

        prev_number = number


if __name__ == "__main__":
    main()
