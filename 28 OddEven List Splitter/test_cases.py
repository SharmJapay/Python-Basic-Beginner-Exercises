"""Test Cases for OddEven List Splitter Exercise"""

import pytest

from main import split_even, split_odd
from input_validation import input_number_list, confirm_exit


def test_input_number_list_valid_number_list(monkeypatch):
    """Test standard behavior when the user inputs a valid number list."""

    # Arrange: Simulate typing '-10, 55, 64, 0, 667' and hitting enter
    monkeypatch.setattr("builtins.input", lambda _: "-10, 55, 64, 0, 667")

    # Act
    result = input_number_list()

    # Assert
    assert result == [-10, 55, 64, 0, 667]


def test_input_number_list_invalid_input_list(monkeypatch, capsys):
    """Test that the loop retries on bad input (different instance items) and succeeds on a valid number list."""

    # Arrange: Simulate typing '-10, asd, 64, /, 667', and then '1, 2, 3, 4, 5'
    inputs = iter(["-10, asd, 64, /, 667", "1, 2, 3, 4, 5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_number_list()

    # Assert
    assert result == [1, 2, 3, 4, 5]

    # Verify that the error message was printed 1 times for the 1 failed attempts
    captured = capsys.readouterr()
    error_msg = "Error! Cannot accept other values except integers only. Try Again."
    assert captured.out.count(error_msg) == 1


def test_input_number_list_invalid_empty_input(monkeypatch, capsys):
    """Test that the loop retries on bad input (empty value) and succeeds on a valid string."""

    # Arrange: Simulate typing '', and then '1, 2, 3, 4, 5'
    inputs = iter(["", "1, 2, 3, 4, 5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    result = input_number_list()

    # Assert
    assert result == [1, 2, 3, 4, 5]

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
    "numbers, expected",
    [
        # Case 1: "[10, 20, 33, 46, 55]" -> Should return [10, 20, 46]
        ([10, 20, 33, 46, 55], [10, 20, 46]),
        # Case 2: "[35, 100, 78, 65, 43]" -> Should return [100, 78]
        ([35, 100, 78, 65, 43], [100, 78]),
        # Case 3: "[15, 91, 87, 61, 121]" -> Should return []
        ([15, 91, 87, 61, 121], []),
        # Case 4: "[54, 72, 28, 188, 220]" -> Should return [54, 72, 28, 188, 220]
        ([54, 72, 28, 188, 220], [54, 72, 28, 188, 220]),
        # Case 5: "[12, 7, 34, 21, 5, 10, 8, 3, 19, 2]" -> Should return [12, 34, 10, 8, 2]
        ([12, 7, 34, 21, 5, 10, 8, 3, 19, 2], [12, 34, 10, 8, 2]),
    ],
)
def test_split_even(numbers, expected):
    """Test that the function correctly outputs the expected value."""

    assert split_even(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        # Case 1: "[10, 20, 33, 46, 55]" -> Should return [33,55]
        ([10, 20, 33, 46, 55], [33, 55]),
        # Case 2: "[35, 100, 78, 65, 43]" -> Should return [35, 65, 43]]
        ([35, 100, 78, 65, 43], [35, 65, 43]),
        # Case 3: "[15, 91, 87, 61, 121]" -> Should return [15, 91, 87, 61, 121]
        ([15, 91, 87, 61, 121], [15, 91, 87, 61, 121]),
        # Case 4: "[54, 72, 28, 188, 220]" -> Should return []
        ([54, 72, 28, 188, 220], []),
        # Case 5: "[12, 7, 34, 21, 5, 10, 8, 3, 19, 2]" -> Should return [7, 21, 5, 3, 19]
        ([12, 7, 34, 21, 5, 10, 8, 3, 19, 2], [7, 21, 5, 3, 19]),
    ],
)
def test_split_odd(numbers, expected):
    """Test that the function correctly outputs the expected value."""

    assert split_odd(numbers) == expected
