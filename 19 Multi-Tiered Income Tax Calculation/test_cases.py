"""Test Cases for Multi-Tiered Income Tax Calculation Exercise"""

import pytest

from main import calculate_tax
from input_validation import input_number, confirm_exit


def test_input_number_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '12' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "12")

    # Act
    result = input_number()

    # Assert
    assert result == 12


def test_input_number_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers) and succeeds on a valid number."""

    # Arrange: Simulate typing 'thing', then '', then '-1', and finally '20'
    inputs = iter(["thing", "", "-1", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_number()

    # Assert
    assert result == 20

    # Verify that the error message was printed 3 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! The input must be positive integer only. Try Again."
    assert captured.out.count(error_msg) == 3


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
    """Test that the loop retries on bad input (empty value and other strings aside from 'yes' or 'no') and succeeds on a 'no' string."""

    # Arrange: Simulate typing 'loops', then '6', then '', then '/-+', and finally 'no'
    inputs = iter(["loops", "6", "", "/-+", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    answer = confirm_exit()

    # Assert
    assert answer == "no"

    # Verify that the error message was printed 4 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Accepts 'Yes' or 'No' values only. Try Again."
    assert captured.out.count(error_msg) == 4


@pytest.mark.parametrize(
    "number, expected",
    [
        # Case 1: 1000 income -> Should return 0 tax
        (1000, 0),
        # Case 2: 10000 income -> Should return 0 tax
        (10000, 0),
        # Case 3: 10001 income -> Should return 0.1 tax
        (10001, 0.1),
        # Case 4: 15000 income -> Should return 500 tax
        (15000, 500),
        # Case 5: 20000 income -> Should return 1000 tax
        (20000, 1000),
        # Case 6: 20001 income -> Should return 1000.2 tax
        (20001, 1000.2),
        # Case 7: 35000 income -> Should return 4000 tax
        (35000, 4000),
        # Case 8: 45000 income -> Should return 6000 tax
        (45000, 6000),
    ],
)
def test_calculate_tax(number, expected):
    """Test that the function correctly outputs the expected value."""

    assert calculate_tax(number) == expected
