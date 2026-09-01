"""Test Cases for Arithmetic Product and Conditional Logic"""

import pytest

from main import compute_product_or_sum_result
from input_validation import get_number, confirm_exit


def test_get_number_invalid_argument(capsys):
    """Test that an invalid argument prints an error and returns None."""

    # Act
    result = get_number("third")

    # Assert
    captured = capsys.readouterr()
    assert "Invalid argument value: 'third'" in captured.out
    assert result is None


def test_get_number_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '5' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "5")

    # Act
    result = get_number("first")

    # Assert
    assert result == 5


def test_get_number_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers, zero) and succeeds on a valid number."""

    # Arrange: Simulate typing 'abc', then '', then '-5', then '0', and finally '10'
    inputs = iter(["abc", "", "-5", "0", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = get_number("second")

    # Assert
    assert result == 10

    # Verify that the error message was printed 4 times for the 4 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! The number must be positive integer value only"
    assert captured.out.count(error_msg) == 4


def test_confirm_exit_yes(monkeypatch):
    """Test standard behavior when the user inputs a 'yes' string."""

    # Arrange: Simulate typing '5' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "yes")

    # Act
    answer = confirm_exit()

    # Assert
    assert answer == "yes"


def test_confirm_exit_no(monkeypatch):
    """Test standard behavior when the user inputs a 'no' string."""

    # Arrange: Simulate typing '5' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "no")

    # Act
    answer = confirm_exit()

    # Assert
    assert answer == "no"


def test_confirm_exit_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value and other strings aside from 'yes' or 'no') and succeeds on a 'yes' string."""

    # Arrange: Simulate typing 'xyz', then '10', then '', and finally 'yes'
    inputs = iter(["xyz", "10", "", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    answer = confirm_exit()

    # Assert
    assert answer == "yes"

    # Verify that the error message was printed 3 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Accepts 'Yes' or 'No' values only. Try Again."
    assert captured.out.count(error_msg) == 3


@pytest.mark.parametrize(
    "first, second, expected",
    [
        # Case 1: Product is well below 1000 -> Should return the product
        (10, 20, 200),
        # Case 2: Product is exactly 1000 (Boundary condition) -> Should return the product
        (20, 50, 1000),
        # Case 3: Product is exactly 1001 (Boundary condition) -> Should return the sum
        (1001, 1, 1002),
        # Case 4: Product is much greater than 1000 -> Should return the sum
        (30, 40, 70),
        # Case 5: Negative numbers (Product is <= 1000) -> Should return the product
        (-5, 10, -50),
        # Case 6: Zero (Product is 0, which is <= 1000) -> Should return the product
        (0, 5000, 0),
    ],
)
def test_compute_product_or_sum_result(first, second, expected):
    """Test that the function correctly switches between product and sum based on the 1000 threshold."""

    assert compute_product_or_sum_result(first, second) == expected
