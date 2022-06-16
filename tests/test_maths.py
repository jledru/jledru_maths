"Test Classes for Maths package"

from src.jledru_maths import Maths


def test_Maths_square():
    "testing square function"
    assert Maths.square(3) == 9
