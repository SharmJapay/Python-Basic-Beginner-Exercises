"""Solution for Finding Common Elements (Intersections) Exercise"""

from input_validation import input_number_list, confirm_exit


def find_common_items(list1: list, list2: list) -> list:
    """Returns a list that contains odd values from list1 and even values from list2

    Arguments
        list1 [list]: First list
        list1 [list]: Second list

    Returns
        [list]: A new list that contains odd values from list1 and even values from list2
    """

    new_list = []

    for item in list1:
        if item in list2:
            new_list.append(item)

    return new_list


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

        new_list1 = find_common_items(list1, list2)
        print(f"\nCommon Elements: {new_list1}")

        # Method 2: Using sets
        new_list2 = list(set(list1) & set(list2))
        print(f"\nCommon Elements: {new_list2}")

        # Checks if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
