"""Test Cases for String Indexing and Even Slicing Exercise"""

import pytest

from input_validation import input_text, confirm_exit


def test_input_text_valid_string(monkeypatch):
    """Test standard behavior when the user inputs a string."""

    # Arrange: Simulate typing 'Learning Python is fun' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "Learning Python is fun")

    # Act
    result = input_text()

    # Assert
    assert result == "Learning Python is fun"


def test_input_text_invalid_empty_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value) and succeeds on a valid string."""

    # Arrange: Simulate typing '', and then 'Hello World'
    inputs = iter(["", "Hello World"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_text()

    # Assert
    assert result == "Hello World"

    # Verify that the error message was printed 1 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Cannot accept empty input value. Try Again."
    assert captured.out.count(error_msg) == 1


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
