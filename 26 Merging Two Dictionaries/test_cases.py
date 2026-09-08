"""Test Cases for Merging Two Dictionaries Exercise"""

import pytest

from main import combine
from input_validation import input_dictionary, confirm_exit


def test_input_dictionary_valid_number_list(monkeypatch):
    """Test standard behavior when the user inputs a valid number list."""

    # Arrange: Simulate typing '"city": "New York", "job": "Engineer"' and hitting enter
    monkeypatch.setattr(
        "builtins.input", lambda _: '"city": "New York", "job": "Engineer"'
    )

    # Act
    result = input_dictionary()

    # Assert
    assert result == {"city": "New York", "job": "Engineer"}


def test_input_dictionary_invalid_input_list(monkeypatch, capsys):
    """Test that the loop retries on bad input (different instance items) and succeeds on a valid number list."""

    # Arrange: Simulate typing '-10, asd, 64, /, 667', and then '"name": "Alice", "age": 25'
    inputs = iter(["-10, asd, 64, /, 667", '"name": "Alice", "age": 25'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_dictionary()

    # Assert
    assert result == {"name": "Alice", "age": 25}

    # Verify that the error message was printed 1 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Wrong format. Try Again."
    assert captured.out.count(error_msg) == 1


def test_input_dictionary_invalid_empty_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value) and succeeds on a valid string."""

    # Arrange: Simulate typing '', and then '"name": "Alice", "age": 25'
    inputs = iter(["", '"name": "Alice", "age": 25'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_dictionary()

    # Assert
    assert result == {"name": "Alice", "age": 25}

    # Verify that the error message was printed 1 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Cannot accept empty input value. Try Again."
    assert captured.out.count(error_msg) == 1


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
    "dict_items1, dict_items2, expected",
    [
        # Case 1: {"name": "Alice", "age": 25}, {"city": "New York", "job": "Engineer"} -> Should return {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"}
        (
            {"name": "Alice", "age": 25},
            {"city": "New York", "job": "Engineer"},
            {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"},
        ),
        # Case 2: {"name": "Alice", "age": 25}, {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'} -> Should return {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"}
        (
            {"name": "Alice", "age": 25},
            {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"},
            {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"},
        ),
    ],
)
def test_combine(dict_items1, dict_items2, expected):
    """Test that the function correctly outputs the expected value."""

    assert combine(dict_items1, dict_items2) == expected
