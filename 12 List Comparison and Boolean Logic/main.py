"""Solution for List Comparison and Boolean Logic Exercise"""

from input_validation import input_number_list, confirm_exit


def is_first_last_item_equal(list_items: list) -> bool:
    """Returns True or False after checking whether first and last item are equal

    Arguments
        list_items [list]: The validated list

    Returns
        [bool]: Boolean value after validation
    """

    first_item = list_items[0]
    last_item = list_items[len(list_items) - 1]

    return first_item == last_item


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        numbers = input_number_list()
        print(f"\nNumbers List: {numbers}")

        print(
            f"\nGiven list: {numbers} | result is {is_first_last_item_equal(numbers)}"
        )

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
