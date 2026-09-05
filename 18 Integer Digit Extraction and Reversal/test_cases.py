"""Test Cases for Integer Digit Extraction and Reversal Exercise"""

import pytest

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
