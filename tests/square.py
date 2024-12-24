
import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
from src.square import Square
@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (2),
        (1.5)
    ])
def test_rectangle_are_positive(first_side):
    print(first_side)
    area = first_side * first_side
    perimetr = (first_side + first_side) * 2
    react = Square(first_side)
    print(area)
    assert react.get_perimetr == perimetr
    assert react.get_area == area





@pytest.mark.parametrize(
    ("first_side"),
    [
        (0),
        (-4)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(first_side, second_side):
    with pytest.raises(ValueError):
        print(first_side, second_side)

        Square(first_side)