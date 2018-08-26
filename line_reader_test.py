import pytest
from pytest import raises
from unittest.mock import MagicMock
from line_reader import file_reader


# First test.
# Test fails. Mock lines could be moved to here to make it pass, but is redundant with the second test and is removed.
# def test_can_call_read_from_file():
#     fr = file_reader("testname")


# Second test.
def test_returns_correct_string(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test_line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = file_reader("fake_name")
    mock_open.assert_called_once_with("fake_name", "r")
    assert result == "test_line"

# Third test.
def test_bad_file_exception(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test_line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = file_reader("fake_name")



