import pytest
from unittest.mock import MagicMock
from line_reader import file_reader


def test_can_call_read_from_file():
    fr = file_reader("testname")


def test_returns_correct_string(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = file_reader("testname")
    mock_open.assert_call_once_with("testname", "r")
    assert result == "testname"



