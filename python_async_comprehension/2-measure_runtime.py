""" async_copmrehension ran from measure_runtime """


import asyncio
import importlib
import time
from typing import Coroutine
async_comprehension: Coroutine = getattr(
    importlib.import_module("1-async_comprehension"), "async_comprehension"
)

async def measure_runtime() -> float:
    """ Measure the runtime of async_generator and return it. """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
