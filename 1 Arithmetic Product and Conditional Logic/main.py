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
        product = first_number * second_number

        if product <= 1000:
            print(f"The result (product) is {product}")
        else:
            print(f"The result (sum) is {first_number + second_number}")

    else:
        print("Something error occured while doing operation")


if __name__ == "__main__":
    main()
