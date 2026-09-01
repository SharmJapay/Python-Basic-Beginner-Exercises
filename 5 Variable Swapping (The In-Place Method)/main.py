"""Solution for Variable Swapping (The In-Place Method) Exercise"""


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    a = 5
    b = 10

    print(f"Before Swap: {a = }, {b = }")

    # Swaps values of two variables
    a, b = b, a

    print(f"After Swap: {a = }, {b = }")


if __name__ == "__main__":
    main()
