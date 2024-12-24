
import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
from src.triangle import Triangle
@pytest.mark.parametrize(
    ("first_side", "second_side", "third_side"),
    [
        (4, 5, 7),
        (3.5, 6.5, 4)
    ])
def test_rectangle_are_positive( first_side, second_side, third_side):
    print(first_side, second_side)
    perimetr = third_side + second_side + first_side
    react = Triangle(first_side, second_side, third_side)
    assert react.get_perimetr == perimetr





@pytest.mark.parametrize(
    ("first_side", "second_side", "third_side"),
    [
        (0, 3, 4),
        (-4, 2.5, -2)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(first_side, second_side, third_side):
    with pytest.raises(ValueError):
        print(first_side, second_side, third_side)

        Triangle(first_side, second_side, third_side)