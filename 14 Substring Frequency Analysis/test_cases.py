"""Test Cases for String Reversal Exercise"""

import pytest

from main import count_words
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


@pytest.mark.parametrize(
    "sentence, substring, expected",
    [
        # --- Original Cases ---
        # Case 1: Multiple occurrences
        ("Emma is good developer. Emma is a writer", "Emma", 2),
        # Case 2: Single occurrence
        ("Hello World! How's everyone doing?", "Hello", 1),
        # --- Case Sensitivity ---
        # Case 3: Case-sensitive mismatch (exact python .count behavior)
        ("Ball is quite popular. The color of the ball is random.", "ball", 1),
        # Case 4: Substring is entirely uppercase
        ("Python is fun. PYTHON is great.", "Python", 1),
        # --- Partial Matches & Compound Words ---
        # Case 5: Substring inside larger words (e.g., "ball" in "Basketball")
        ("Basketball, Volleyball, Soccer, football.", "ball", 3),
        # Case 6: Substring attached to punctuation / possessives
        ("The ball's shape is a circle.", "ball", 1),
        # --- Edge Cases & No Matches ---
        # Case 7: Substring not present at all
        ("The quick brown fox jumps over the lazy dog.", "cat", 0),
        # Case 8: Searching within an empty string
        ("", "apple", 0),
        # Case 9: The entire string is the substring
        ("Python", "Python", 1),
        # --- Overlapping Substrings ---
        # Case 10: Overlapping patterns (Standard .count() handles non-overlapping)
        # Note: Change expected to 2 if your custom count_words handles overlapping!
        ("banana", "ana", 1),
    ],
)
def test_reverse(sentence, substring, expected):
    """Test that the function correctly outputs the expected value."""

    assert count_words(sentence, substring) == expected
