
import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
import math
from src.circle import Circle
@pytest.mark.parametrize(
    ("radius"),
    [
        (2),
        (1.7)
    ])
def test_circle_are_positive(radius):
    print(radius)
    area = math.pi * (radius ** 2)
    react = Circle(radius)
    print(area)
    assert react.get_area == area





@pytest.mark.parametrize(
    ("radius"),
    [
        (0),
        (-4)
    ],
    ids=["zero value", "negative value"]
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        print(radius)
        Circle(radius)