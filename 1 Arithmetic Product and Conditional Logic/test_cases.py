"""Test Cases for Arithmetic Product and Conditional Logic"""

import pytest

from main import get_number, compute_product_or_sum_result


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
    """Test that the loop retries on bad input (letters, negative numbers, zero) and succeeds on a valid number."""
    # Arrange: Simulate typing 'abc', then '-5', then '0', and finally '10'
    inputs = iter(["abc", "-5", "0", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = get_number("second")

    # Assert
    assert result == 10

    # Verify that the error message was printed 3 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! The number must be positive integer value only"
    assert captured.out.count(error_msg) == 3
