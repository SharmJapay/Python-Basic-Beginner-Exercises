"""Solution for Merging Lists with Parity Filtering Exercise"""

from input_validation import input_number_list, confirm_exit


def create_odd_even_list(list1: list, list2: list) -> list:
    """Returns a list that contains odd values from list1 and even values from list2

    Arguments
        list1 [list]: First list
        list2 [list]: Second list

    Returns
        [list]: A new list that contains odd values from list1 and even values from list2
    """

    odd_list = [item for item in list1 if item % 2 != 0]
    even_list = [item for item in list2 if item % 2 == 0]

    return odd_list + even_list


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        list1 = input_number_list()
        print(f"\nNumber List1: {list1}")

        list2 = input_number_list()
        print(f"\nNumber List2: {list2}")

        new_list = create_odd_even_list(list1, list2)
        print(f"\nNew List: {new_list}")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
