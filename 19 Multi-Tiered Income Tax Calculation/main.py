"""Solution for Multi-Tiered Income Tax Calculation Exercise"""

from input_validation import input_number, confirm_exit


def calculate_tax(income: int) -> int:
    """Returns the tax value calculated from income

    Arguments
        income [int]: The income value

    Returns
        [int] - The tax value calculated from income
    """

    first_criteria, second_criteria = 10000, 10000

    if income <= first_criteria:
        return 0

    else:
        taxable = income - first_criteria

        if taxable <= second_criteria:
            return (income - 10000) * 0.1

        else:
            excess_taxable = taxable - second_criteria

            return (second_criteria * 0.1) + (excess_taxable * 0.2)


def main() -> None:
    """Starts the program and executes the applications flow

    Returns
        None
    """

    while True:
        income = input_number()
        print(f"\nThe income is ₱{income:.2f}")

        tax_price = calculate_tax(income)

        print(f"\nTotal income tax to pay is ₱{tax_price:.2f}")

        # Check if user wants to exit program
        quit_program = confirm_exit()

        if quit_program.lower() == "yes":
            break


if __name__ == "__main__":
    main()
