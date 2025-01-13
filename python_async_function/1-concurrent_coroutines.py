#!/usr/bin/env python3
import asyncio
from typing import List
import importlib


# Dynamically import wait_random
wait_random = getattr(importlib.import_module("0-basic_async_syntax"), "wait_random")


"""
Module contains the `wait_n` coroutine that runs multiple `wait_random`
coroutines concurrently w/ a max delay and returns their results in
ascending order. Demonstrates asynchronous programming using asyncio and random
delays
"""


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Coroutine spawns `n` wait_random coroutines w/ a max_delay n returns result

    Args:
        n (int): number of wait_random coroutines to run at same time
        max_delay (int): Maximum delay for the random numbers.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    delays = await asyncio.gather(*tasks)
    
    return sorted(delays)
