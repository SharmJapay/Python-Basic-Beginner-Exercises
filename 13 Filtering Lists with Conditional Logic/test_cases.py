"""Test Cases for Filtering Lists with Conditional Logic Exercise"""

import pytest

from main import divisible_by_five
from input_validation import confirm_exit


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
    "list_items, expected",
    [
        # Case 1: "[100, 200, 340, 540, 100]" -> Should return [10, 20, 55]
        ([10, 20, 33, 46, 55], [10, 20, 55]),
        # Case 2: "[35, 10, 78, 65, 45]" -> Should return False [35, 100, 65, 55]
        ([35, 100, 78, 65, 43], [35, 100, 65]),
    ],
)
def test_divisible_by_five(list_items, expected):
    """Test that the function correctly outputs the expected value."""

    assert divisible_by_five(list_items) == expected
