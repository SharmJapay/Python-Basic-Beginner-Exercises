"""Test Cases for Custom Exponentiation Function Exercise"""

import pytest

from main import exponent
from input_validation import input_number, confirm_exit


def test_input_number_invalid_argument(capsys):
    """Test that an invalid argument prints an error and returns None."""

    # Act
    result = input_number("third")

    # Assert
    captured = capsys.readouterr()
    assert "Invalid argument value: 'third'" in captured.out
    assert result is None


def test_input_number_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '5' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "5")

    # Act
    result = input_number("base")

    # Assert
    assert result == 5


def test_input_number_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers, zero) and succeeds on a valid number."""

    # Arrange: Simulate typing 'abc', then '', then '-5', then '0', and finally '10'
    inputs = iter(["abc", "", "-5", "0", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_number("exponent")

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
    "base, exp, expected",
    [
        # Case 1: Base 2, Exponent 6 -> Should return 64
        (2, 6, 64),
        # Case 2: Base 5, Exponent 5 -> Should return 3125
        (5, 5, 3125),
        # Case 3: Base 3, Exponent 4 -> Should return 81
        (3, 4, 81),
        # Case 4: Base 10, Exponent 3 -> Should return 1000
        (10, 3, 1000),
    ],
)
def test_exponent(base, exp, expected):
    """Test that the function correctly switches between product and sum based on the 1000 threshold."""

    assert exponent(base, exp) == expected
