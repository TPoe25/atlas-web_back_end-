#!/usr/bin/env python3
""" An async generator is a function that returns an async generator iterator.
"""


import asyncio
import random
from typing import AsyncGenerator



async def async_generator() -> AsyncGenerator[float, None]:
    """ An async generator that yields 10 random numbers between 0 and 10, sleeping for 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
