
import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
from src.rectangle import Rectangle
@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (2, 3),
        (1.5, 6.5)
    ])
def test_rectangle_are_positive( first_side, second_side):
    print(first_side, second_side)
    area = first_side * second_side
    perimetr = (first_side + second_side) * 2
    react = Rectangle(first_side, second_side)
    print(area)
    assert react.get_perimetr == perimetr
    assert react.get_area == area





@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (0, 3),
        (-4, 2.5)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(first_side, second_side):
    with pytest.raises(ValueError):
        print(first_side, second_side)

        Rectangle(first_side, second_side)
