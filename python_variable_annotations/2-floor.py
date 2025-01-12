#!/usr/bin/env python3
"""
Module w/ a type-annotated function that computes the floor of a float
"""


import math


def floor(n: float) -> int:
    """
    Computes the floor of a float.


    Args:
        n (float): paramater number to compute the floor of a float

    Returns:
        int: floor of the number as a interger
    """
    return math.floor(n)
