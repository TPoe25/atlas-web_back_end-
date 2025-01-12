#!/usr/bin/env python3
"""
defines a func to_kv that takes a str k an an int or flt v
and returns a turple where the first element is the str k and
the second element is the square of v as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the str k and
    the second element is the square of v as a float.

    Args:
        k (str): Key for the tuple.
        v (int or float): Value for the tuple.

    Returns:
        tuple: A tuple containing the key and the square of the value.
    """
    return (k, float(v ** 2))
