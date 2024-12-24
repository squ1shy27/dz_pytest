import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)
# Квадрат
# Прямоугольник
from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, first_side):
        if first_side <= 0:
            raise ValueError("side cant be < 0")
        super().__init__(first_side, first_side)

    @property
    def get_perimetr(self):
        return self.first_side * 4

    @property
    def get_area(self):
        return self.first_side * self.first_side
