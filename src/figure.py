import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)

class Figure:

    @property
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("not a Figure")
        return self.get_area + other_figure.get_area
