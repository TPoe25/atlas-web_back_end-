#!/usr/bin/env python3
"""
Returns a function that multiplies a float by a multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        A func that multiplies a float by the multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
