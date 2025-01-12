#!/usr/bin/env python3
"""
Module that defines a func sum_list that takes list and returns sum as float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all elements in a list.

    Args:
        input_list (list): List of floats to be summed.

    Returns:
        Sum of the floats as a float.
    """
    return sum(input_list)
