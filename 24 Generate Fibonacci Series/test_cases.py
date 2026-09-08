"""Test Cases for Generate Fibonacci Series Exercise"""

import pytest

from main import fibonacci_series
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

    # Arrange: Simulate typing 'yes' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "yes")

    # Act
    answer = confirm_exit()

    # Assert
    assert answer == "yes"


def test_confirm_exit_no(monkeypatch):
    """Test standard behavior when the user inputs a 'no' string."""

    # Arrange: Simulate typing 'no' and hitting enter
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
        # Case 1: 0 -> Should return [0, 1]
        (0, [0, 1]),
        # Case 2: 1 -> Should return [0, 1]
        (1, [0, 1]),
        # Case 3: 2 -> Should return [0, 1]
        (2, [0, 1]),
        # Case 4: 3 -> Should return [0, 1, 1]
        (3, [0, 1, 1]),
        # Case 5: 4 -> Should return [0, 1, 1, 2]
        (4, [0, 1, 1, 2]),
        # Case 6: 15 -> Should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]),
    ],
)
def test_fibonacci_series(number, expected):
    """Test that the function correctly outputs the expected value."""

    assert fibonacci_series(number) == expected
