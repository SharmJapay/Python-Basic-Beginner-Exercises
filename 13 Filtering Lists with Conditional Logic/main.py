"""Solution for Filtering Lists with Conditional Logic Exercise"""

from input_validation import input_number_list, confirm_exit


def divisible_by_five(list_items: list) -> list:
    """Returns a list that contains numbers divisible by 5

    Arguments
        list_items [list]: The validated list

    Returns
        [list]: A new list that contains numbers divisible by 5
    """
    validated_list = []

    for item in list_items:
        if item % 5 == 0:
            validated_list.append(item)

    return validated_list


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        number_list = input_number_list()
        print(f"\nNumber List: {number_list}")

        new_list = divisible_by_five(number_list)

        print("\nDivisible by 5:")
        print(str(new_list).strip("[").strip("]"))

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
