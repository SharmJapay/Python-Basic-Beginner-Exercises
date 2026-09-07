"""Solution for Generate Fibonacci Series Exercise"""

from input_validation import input_number, confirm_exit


def fibonacci_series(number: int) -> list:
    """Returns a list of fibonacci series

    Arguments
        number [int]: The number of terms in fibonacci series

    Returns
        [list] - The list of fibonacci series
    """

    fibonacci = [0, 1]

    if number <= 2:
        return fibonacci

    for index in range(number - 2):
        first_num = fibonacci[index]
        second_num = fibonacci[index + 1]

        fibonacci.append(first_num + second_num)

    return fibonacci


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        number = input_number()

        print(f"\nNumber of terms:  {number}")

        sequence = fibonacci_series(number)

        print("\nFibonacci Series: ")

        for item in sequence:
            print(item, end=" ")

        print("\n", end="")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
