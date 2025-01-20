#!/usr/bin/env python3i
"""
 A coroutine that waits for a random delay btwn 0 n max_delay secs n rtn delay
"""


from typing import List
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
