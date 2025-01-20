#!/usr/bin/env python3
"""
Demonstrates asynchronous programming using asyncio and random
delays
"""

from typing import List
import asyncio
import importlib
# Dynamically import wait_random
wait_random = getattr(importlib.import_module("0-basic_async_syntax"),
                      "wait_random")


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Coroutine spawns `n` wait_random coroutines w/ a max_delay n returns result

    Args:
        n (int): number of wait_random coroutines to run at same time
        max_delay (int): Maximum delay for the random numbers.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delay = []
    for task in asyncio.as_completed(delays):
        completed_delay.append(await task)

    return completed_delay
