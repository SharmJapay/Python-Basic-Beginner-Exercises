"""Test Cases for Word Length Analysis Exercise"""

import pytest

from input_validation import input_string_list, confirm_exit


def test_input_string_list_valid_string_list(monkeypatch):
    """Test standard behavior when the user inputs a valid string list."""

    # Arrange: Simulate typing "'apple', 'banana', 'cherry'" and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "'apple', 'banana', 'cherry'")

    # Act
    result = input_string_list()

    # Assert
    assert result == ["apple", "banana", "cherry"]


def test_input_string_list_invalid_input_list(monkeypatch, capsys):
    """Test that the loop retries on bad input (some items are empty) and succeeds on a valid string list."""

    # Arrange: Simulate typing 'hello, asd, , , 667', then ' , , , ' and then 'a1, b2, c3, d4, e5'
    inputs = iter(["hello, asd, , , 667", " , , , ", "a1, b2, c3, d4, e5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_string_list()

    # Assert
    assert result == ["a1", "b2", "c3", "d4", "e5"]

    # Verify that the error message was printed 2 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Found an empty value item. Try Again."
    assert captured.out.count(error_msg) == 2


def test_input_string_list_invalid_empty_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value) and succeeds on a valid string."""

    # Arrange: Simulate typing '', and then 'ant, bat, car, drone, egg'
    inputs = iter(["", "ant, bat, car, drone, egg"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_string_list()

    # Assert
    assert result == ["ant", "bat", "car", "drone", "egg"]

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
