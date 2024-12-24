# Круг
import math
from figure import Figure
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("radius cant be < 0")
        self.radius = radius

    @property
    def get_area(self):
        return math.pi * (self.radius ** 2)

    @property
    def get_perimetr(self):
        return 2 * math.pi * self.radius




