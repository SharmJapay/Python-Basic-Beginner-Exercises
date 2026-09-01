"""Solution for Arithmetic Product and Conditional Logic"""


def get_number(place: str) -> int | None:
    """Returns a valid integer value if input conditions are met, otherwise None

    Arguments
        place [str]: The value must be 'first' or 'second' only

    Returns
        number [int] or None
    """

    if place not in ["first", "second"]:
        print(f"Invalid argument value: '{place}'")
        return

    while True:
        try:
            number = int(input(f"Enter {place} number: "))

            if 0 >= number:
                raise ValueError

            break

        except ValueError:
            print("Error! The number must be positive integer value only")
            continue

    return number


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

    Arguments
        None

    Returns
        None
    """

    first_number = get_number("first")
    second_number = get_number("second")

    if first_number and second_number:
        result = compute_product_or_sum_result(first_number, second_number)
        print(f"The result is {result}")

    else:
        print("Something error occured while doing operation")


if __name__ == "__main__":
    main()
