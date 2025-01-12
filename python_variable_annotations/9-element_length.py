#!/usr/bin/env python3
"""
Returns a list of tuples that contains an item from the iterable and length
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples that contains an item from iterable and length

    Args:
        lst: Iterable to iterate over

    Returns:
        List of tuples containing items and their lengths
    """
    return [(i, len(i)) for i in lst]
