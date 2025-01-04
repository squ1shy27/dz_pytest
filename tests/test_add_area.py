import pytest
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (2, 3),
        (1.5, 6.5)
    ])
def test_add_area_rectangle_to_rectangle(first_side, second_side):
    rect1 = Rectangle(first_side, second_side)
    #Создаем еще один прямоугольник для теста
    rect2 = Rectangle(4, 5)
    expected_area = rect1.get_area + rect2.get_area
    assert rect1.add_area(rect2) == expected_area


@pytest.mark.parametrize(
    ("first_side"),
    [
        (3),
        (5.5)
    ])
def test_add_area_square_to_square(first_side):
    square1 = Square(first_side)
    #Создаем еще один квадрат для теста
    square2 = Square(4)
    expected_area = square1.get_area + square2.get_area
    assert square1.add_area(square2) == expected_area


@pytest.mark.parametrize(
    ("first_side", "second_side"),
    [
        (2, 3),
        (1.5, 6.5)
    ])
def test_add_area_rectangle_to_square(first_side, second_side):
    rect = Rectangle(first_side, second_side)
    #Создаем квадрат для теста
    square = Square(4)
    expected_area = rect.get_area + square.get_area
    assert rect.add_area(square) == expected_area


@pytest.mark.parametrize(
    ("first_side"),
    [
        (3),
        (5.5)
    ])
def test_add_area_square_to_rectangle(first_side):
    square = Square(first_side)
    # Создаем прямоугольник для теста
    rect = Rectangle(4, 5)
    expected_area = square.get_area + rect.get_area
    assert square.add_area(rect) == expected_area