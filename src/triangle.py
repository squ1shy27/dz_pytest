from figure import Figure
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
import math


# Треугольник
class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        if second_side <= 0 or first_side <= 0 or third_side <= 0:
            raise ValueError("side cant be < 0")
        elif second_side + first_side <= third_side or second_side + third_side <= first_side or first_side + third_side <= second_side:
            raise ValueError("Cant be triangle")
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    @property
    def get_perimetr(self):
        """Периметр треугольника"""
        p = self.third_side + self.second_side + self.first_side
        return p

    @property
    def get_area(self):
        """Площадь треугольника"""
        s = self.get_perimetr / 2
        return math.sqrt(s * (s - self.first_side) * (s - self.second_side) * (s - self.third_side))


triangle = Triangle(5, 7, 9)
