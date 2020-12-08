import unittest
import pytest

from andrew_is_hungry_for_py.eat import feedme


@pytest.mark.parametrize("input_date,expected", [
    ("2019-10-31", "Birthday Cake"),
    ("2019-10-01", "Cake"),
    ("2019-11-01", "Leftover Birthday Cake"),
    ("2020-10-31", "Birthday Cake"),
    ("2020-11-14", "Stale Birthday Cake"),
])
def test_feedme(input_date, expected):
    assert feedme(input_date) == expected
