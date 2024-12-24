import pytest
import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_LOG = os.path.dirname(os.path.abspath(ROOT_DIR))
sys.path.append(PATH_LOG)

@pytest.fixture(scope="function", autouse=True)
def mark():
    print("\n______Start______")
    yield
    print("\n______Stop______")


