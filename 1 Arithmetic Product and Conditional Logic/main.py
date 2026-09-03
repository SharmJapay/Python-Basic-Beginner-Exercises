"""Solution for Arithmetic Product and Conditional Logic Exercise"""

from input_validation import input_number, confirm_exit


def compute_product_or_sum_result(first_number: int, second_number: int) -> int:
    """Return product of two numbers if the result is less than or equal to 1000, otherwise return sum.

    Arguments
        first_number [int]: The first value for calculation
        second_number [int]: The second value for calculation

    Returns
        [int] - The integer value of product or sum result
    """

    if first_number * second_number <= 1000:
        return first_number * second_number

    else:
        return first_number + second_number


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """
    while True:
        first_number = input_number("first")
        second_number = input_number("second")

        if first_number and second_number:
            result = compute_product_or_sum_result(first_number, second_number)
            print(f"The result is {result}")

        else:
            print("Something error occured while doing operation")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
