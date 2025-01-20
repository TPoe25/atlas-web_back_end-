#!/usr/bin/env python3
""" Measure the runtime of wait_n
"""


import asyncio
from time import perf_counter
import importlib
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ takes int n and max_delay for execution time_
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return total_time / n
