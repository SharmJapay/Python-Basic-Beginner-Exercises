"""Test Cases for Word Frequency Counter (The Histogram) Exercise"""

import pytest

from main import word_counter
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
    "text, expected",
    [
        # Case 1: "apple Banana Apple Cherry banana apple Date fig Date Elderberry" (without extra whitespaces) -> Should return "{'apple': 3, 'banana': 2, 'cherry': 1, 'date': 2, 'fig': 1, 'elderberry': 1}"
        (
            "apple Banana Apple Cherry banana apple Date fig Date Elderberry",
            {
                "apple": 3,
                "banana": 2,
                "cherry": 1,
                "date": 2,
                "fig": 1,
                "elderberry": 1,
            },
        ),
        # Case 2: "  apple   banana apple cherry   banana apple   Date fig Date Elderberry" (with extra whitespaces) -> Should return "{'apple': 3, 'banana': 2, 'cherry': 1, 'date': 2, 'fig': 1, 'elderberry': 1}"
        (
            "  apple   banana apple cherry   banana apple   Date fig Date Elderberry",
            {
                "apple": 3,
                "banana": 2,
                "cherry": 1,
                "date": 2,
                "fig": 1,
                "elderberry": 1,
            },
        ),
    ],
)
def test_word_counter1(text, expected):
    """Test that the function correctly outputs the expected value."""

    assert word_counter(text) == expected


@pytest.mark.parametrize(
    "text, state, expected",
    [
        # Case 1: "apple Banana Apple Cherry banana apple Date fig Date Elderberry" (without extra whitespaces) -> Should return "{'apple': 3, 'banana': 2, 'cherry': 1, 'date': 2, 'fig': 1, 'elderberry': 1}"
        (
            "apple Banana Apple Cherry banana apple Date fig Date Elderberry",
            "case_sensitive",
            {
                "apple": 2,
                "Banana": 1,
                "Apple": 1,
                "Cherry": 1,
                "banana": 1,
                "Date": 2,
                "fig": 1,
                "Elderberry": 1,
            },
        ),
        # Case 2: "  apple   banana apple cherry   banana apple   Date fig date Elderberry" (with extra whitespaces) -> Should return "{'apple': 3, 'banana': 2, 'cherry': 1, 'date': 2, 'fig': 1, 'elderberry': 1}"
        (
            "  apple   Banana Apple Cherry   banana apple   Date fig Date Elderberry",
            "case_sensitive",
            {
                "apple": 2,
                "Banana": 1,
                "Apple": 1,
                "Cherry": 1,
                "banana": 1,
                "Date": 2,
                "fig": 1,
                "Elderberry": 1,
            },
        ),
    ],
)
def test_word_counter2(text, state, expected):
    """Test that the function correctly outputs the expected value."""

    assert word_counter(text, state) == expected
