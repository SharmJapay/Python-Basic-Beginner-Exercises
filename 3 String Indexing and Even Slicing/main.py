"""Solution for String Indexing and Even Slicing"""


def main() -> None:
    """Starts the program and executes the applications flow"""

    text = "Learning Python is fun"
    even_chars = text[0::2]

    print(f"Original String is '{text}'")
    print("Printing only even index chars")

    for char in even_chars:
        print(char)


if __name__ == "__main__":
    main()
