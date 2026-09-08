"""Solution for Merging Two Dictionaries Exercise"""

from input_validation import input_dictionary, confirm_exit


def combine(dict_items1: dict, dict_items2: dict) -> dict:
    """Returns a list that contains numbers divisible by 5

    Arguments
        dict_items1 [dict]: The first list
        dict_items2 [dict]: The second list

    Returns
        [dict]: A new dictionary that contains items from first and second dictionaries
    """

    return dict_items1 | dict_items2


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:

        dictionary1 = input_dictionary()
        print(f"\nDictionary1: \n{dictionary1}")

        dictionary2 = input_dictionary()
        print(f"\nDictionary2: \n{dictionary2}")

        new_dict = combine(dictionary1, dictionary2)

        print("\nCombined Dictionaries:")
        print(new_dict)

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
