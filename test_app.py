# Use pytest to test the function `add` from the `app` module
import pytest

from app import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 7, 7),
        (1.5, 2.25, 3.75),
    ],
)
def test_add_numbers(a, b, expected):
    assert add(a, b) == expected


def test_add_strings():
    assert add("GitHub ", "Copilot") == "GitHub Copilot"

print("All tests passed!")
