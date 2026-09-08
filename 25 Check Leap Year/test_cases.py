"""Test Cases for Check Leap Year Exercise"""

import pytest

from main import is_leap
from input_validation import input_year, confirm_exit


def test_input_year_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '12' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "12")

    # Act
    result = input_year()

    # Assert
    assert result == 12


def test_input_year_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers, zero) and succeeds on a valid number."""

    # Arrange: Simulate typing 'thing', then '', then '-1', then '0', and finally '20'
    inputs = iter(["thing", "", "-1", "0", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_year()

    # Assert
    assert result == 20

    # Verify that the error message was printed 4 times for the 4 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! The year must be greater than 0. Try Again."
    assert captured.out.count(error_msg) == 4


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

    # Verify that the error message was printed 4 times for the 4 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Accepts 'Yes' or 'No' values only. Try Again."
    assert captured.out.count(error_msg) == 4


@pytest.mark.parametrize(
    "year, expected",
    [
        # Case 1: 2024 -> Should return True
        (2024, True),
        # Case 2: 1111 -> Should return False
        (1111, False),
        # Case 3: 2000 -> Should return True
        (2000, True),
        # Case 4: 1900 -> Should return False
        (1900, False),
        # Case 5: 1644 -> Should return True
        (1644, True),
        # Case 6: 1888 -> Should return True
        (1888, True),
    ],
)
def test_is_leap(year, expected):
    """Test that the function correctly outputs the expected value."""

    assert is_leap(year) == expected
