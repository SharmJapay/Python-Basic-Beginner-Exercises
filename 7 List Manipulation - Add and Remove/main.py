"""Solution for List Manipulation - Add or Remove Exercise"""

from input_validation import input_item, input_index_number, do_action, confirm_exit


def add_item(list_items: list, item: str) -> list:
    """Returns an updated list with new item

    Arguments
        list_items [list]: The list that will be updated
        item [str]: The value that will be added to the list

    Returns
        [list]: A new list that is updated with new item
    """

    list_items.append(item)
    return list_items


def remove_item(list_items: list, index: int) -> list:
    """Returns an updated list with an item removed

    Arguments
        list_items [list]: The list that will be updated
        index [int]: The index of the list that will be removed

    Returns
        [list]: A new list that is updated with an item removed
    """

    list_items.pop(index)
    return list_items


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"\nOriginal Fruit List: {fruits}")

    while True:
        action = do_action()

        if action.lower() == "add":
            fruit = input_item()
            fruits = add_item(fruits, fruit)
            print(f"\nNew Fruit List: {fruits}\n")

        elif action.lower() == "remove":
            index = input_index_number()

            if index <= len(fruits) - 1:
                fruit = fruits[index]
                fruits = remove_item(fruits, index)

                print(
                    f"\nThe fruit '{fruit}' in the index '{index}' has been removed from the list\n"
                )
                print(f"New Fruit List: {fruits}\n")

            else:
                print(
                    f"\nCannot delete a fruit in index '{index}' because it is out of range in list.\n"
                )
                print(f"Fruit List is still: {fruits}\n")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
