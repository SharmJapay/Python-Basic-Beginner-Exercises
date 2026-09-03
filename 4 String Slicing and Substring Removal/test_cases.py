"""Test Cases for String Slicing and Substring Removal Exercise"""

import pytest

from input_validation import (
    input_text,
    input_index_number,
    input_position,
    remove_chars,
    confirm_exit,
)


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

    # Arrange: Simulate typing '', then '  ', and finally 'Hello World'
    inputs = iter(["", "  ", "Hello World"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_text()

    # Assert
    assert result == "Hello World"

    # Verify that the error message was printed 2 times for the 2 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Cannot accept empty input value. Try Again."
    assert captured.out.count(error_msg) == 2


def test_input_index_number_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '25' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "25")

    # Act
    result = input_index_number()

    # Assert
    assert result == 25


def test_input_index_number_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers) and succeeds on a valid number."""

    # Arrange: Simulate typing 'abc', then '', then '-5', and finally '36'
    inputs = iter(["abc", "", "-5", "36"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_index_number()

    # Assert
    assert result == 36

    # Verify that the error message was printed 3 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! The input must be positive integer only. Try Again."
    assert captured.out.count(error_msg) == 3


def test_input_position_valid_start_string(monkeypatch):
    """Test standard behavior when the user inputs a 'start' string."""

    # Arrange: Simulate typing 'start' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "start")

    # Act
    answer = input_position()

    # Assert
    assert answer == "start"


def test_input_position_valid_end_string(monkeypatch):
    """Test standard behavior when the user inputs a 'end' string."""

    # Arrange: Simulate typing 'end' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "end")

    # Act
    answer = input_position()

    # Assert
    assert answer == "end"


def test_input_position_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value and other strings aside from 'start' or 'end') and succeeds on a 'end' string."""

    # Arrange: Simulate typing 'xyz', then '10', then '', and finally 'end'
    inputs = iter(["xyz", "10", "", "end"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    answer = input_position()

    # Assert
    assert answer == "end"

    # Verify that the error message was printed 3 times for the 3 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Accepts 'Start' or 'End' values only. Try Again."
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
    "text, index, position, expected",
    [
        # Case 1: Length of text is greater than index, index is positive integer 4, position is 'start' -> Should return string
        ("Coding with Python is fun", 4, "start", "ng with Python is fun"),
        # Case 2: Length of text is greater than index, index is positive integer 2, position is 'end' -> Should return string
        ("Coding with Python is fun", 2, "end", "Coding with Python is f"),
        # Case 3: Length of text is greater than index, index is positive integer 0, position is 'start' -> Should return string
        ("Hello", 0, "start", "Hello"),
        # Case 4: Length of text is greater than index, index is positive integer 0, position is 'end' -> Should return string
        ("Hello", 0, "end", "Hello"),
        # Case 5: Length of text is equal to index, index is positive integer 5, position is 'start' -> Should return empty ""
        ("Hello", 5, "start", ""),
        # Case 6: Length of text is equal to index, index is positive integer 5, position is 'end' -> Should return empty ""
        ("Hello", 5, "end", ""),
        # Case 7: Length of text is equal to index, index is positive integer 5, position is 'start' -> Should return empty ""
        ("Hello World!", 20, "start", ""),
        # Case 8: Length of text is equal to index, index is positive integer 5, position is 'end' -> Should return empty ""
        ("Hello World!", 20, "end", ""),
    ],
)
def test_remove_chars(text, index, position, expected):
    """Test that the function correctly removes chars in the original text."""

    assert remove_chars(text, index, position) == expected
