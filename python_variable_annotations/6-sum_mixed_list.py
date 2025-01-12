#!/usr/bin/env python3
"""
Module sum_mixed_list takes a list of ints and floats then returns sum as flt
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of all elements in a list.

    Args:
        mixed_list (list): List of ints and floats to be summed.
    Returns:
        Sum of the ints and floats as a float.
    """
    return float(sum(mxd_list))
