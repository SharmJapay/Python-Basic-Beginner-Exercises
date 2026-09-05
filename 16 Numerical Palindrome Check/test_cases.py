"""Test Cases for Numerical Palindrome Check Exercise"""

import pytest

from main import is_palindrome
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
        # Case 1: integer 1 -> Should return 1
        (121, True),
        # Case 2: integer 2 -> Should return 1
        (125, False),
        # Case 3: integer 3 -> Should return 2
        (252, True),
        # Case 4: integer 4 -> Should return 6
        (13231, True),
        # Case 5: integer 5 -> Should return 24
        (789, False),
        # Case 6: integer 6 -> Should return 120
        (4567654, True),
        # Case 7: integer 6 -> Should return 720
        (876, False),
        # Case 8: integer 6 -> Should return 5040
        (357, False),
    ],
)
def test_is_palindrome(number, expected):
    """Test that the function correctly outputs the expected value."""

    assert is_palindrome(number) == expected
