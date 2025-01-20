#!/usr/bin/env python3
import asyncio
import random
"""
A coroutine that waits froa a random delay btwn 0 n max_delay secs n rtn delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
        max_delay (int): Max delay in seconds. Defaults to 10.

    Returns:
        float: Random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
