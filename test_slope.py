# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:03:34 2023

@author: lilbl
"""
import pytest

@pytest.mark.parametrize("xs", "ys", "newx", "expected",
                         [((0,1), (0,1), 2, 2),
                          ((1,2), (2,4), 2, 4),
                          ((2,5), (3,9), -2, -11),
                          ((2,5), (4,6), 1, 4.5)])
def test_slope(xs, ys, newx, expected):
    from check_slope import slope
    answer=slope(xs, ys, newx)
    assert answer == expected
    