"""Test Cases for List Manipulation - Add or Remove Exercise"""

import pytest

from main import add_item, remove_item
from input_validation import input_item, input_index_number, confirm_exit


def test_input_item_valid_string(monkeypatch):
    """Test standard behavior when the user inputs a string."""

    # Arrange: Simulate typing 'fig' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "fig")

    # Act
    result = input_item()

    # Assert
    assert result == "fig"


def test_input_item_invalid_empty_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value) and succeeds on a valid string."""

    # Arrange: Simulate typing '', and then 'grape'
    inputs = iter(["", "grape"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_item()

    # Assert
    assert result == "grape"

    # Verify that the error message was printed 1 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Cannot accept empty input value. Try Again."
    assert captured.out.count(error_msg) == 1


def test_input_index_number_valid_first_try(monkeypatch):
    """Test standard behavior when the user inputs a valid positive integer immediately."""

    # Arrange: Simulate typing '2' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "2")

    # Act
    result = input_index_number()

    # Assert
    assert result == 2


def test_input_index_number_retries_on_invalid_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (letters, empty value, negative numbers) and succeeds on a valid number."""

    # Arrange: Simulate typing 'thing', then '', then '-1', and finally '0'
    inputs = iter(["thing", "", "-1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_index_number()

    # Assert
    assert result == 0

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
    "list_items, item, expected",
    [
        # Case 1: "fig" -> Should return '["apple", "banana", "cherry", "date", "elderberry", "fig"]'
        (
            ["apple", "banana", "cherry", "date", "elderberry"],
            "fig",
            ["apple", "banana", "cherry", "date", "elderberry", "fig"],
        ),
        # Case 2: "grape" -> Should return '["apple", "banana", "cherry", "date", "elderberry", "grape"]'
        (
            ["apple", "banana", "cherry", "date", "elderberry"],
            "grape",
            ["apple", "banana", "cherry", "date", "elderberry", "grape"],
        ),
    ],
)
def test_add_item(list_items, item, expected):
    """Test that the function correctly outputs the expected value."""

    assert add_item(list_items, item) == expected


@pytest.mark.parametrize(
    "list_items, index, expected",
    [
        # Case 1: "fig" -> Should return '["apple", "banana", "cherry", "date", "elderberry", "fig"]'
        (
            ["apple", "banana", "cherry", "date", "elderberry"],
            0,
            ["banana", "cherry", "date", "elderberry"],
        ),
        # Case 2: "grape" -> Should return '["apple", "banana", "cherry", "date", "elderberry", "grape"]'
        (
            ["apple", "banana", "cherry", "date", "elderberry"],
            2,
            ["apple", "banana", "date", "elderberry"],
        ),
    ],
)
def test_remove_item(list_items, index, expected):
    """Test that the function correctly outputs the expected value."""

    assert remove_item(list_items, index) == expected
