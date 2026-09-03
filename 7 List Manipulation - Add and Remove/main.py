"""Solution for List Manipulation - Add or Remove Exercise"""

from input_validation import input_item, input_index_number, do_action, confirm_exit


def main() -> None:
    """Starts the program and executes the applications flow"""

    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"\nOriginal Fruit List: {fruits}")

    while True:
        action = do_action()

        if action.lower() == "add":
            fruit = input_item()
            fruits.append(fruit)
            print(f"\nNew Fruit List: {fruits}\n")

        elif action.lower() == "remove":
            index = input_index_number()

            if index <= len(fruits) - 1:
                fruit = fruits[index]
                fruits.pop(index)

                print(
                    f"\nThe fruit {fruit} in the index {index} has been removed from the list\n"
                )
                print(f"New Fruit List: {fruits}\n")

            else:
                print(
                    f"\nCannot delete a fruit in index {index} because it is out of range in list.\n"
                )
                print(f"Fruit List is still: {fruits}\n")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
