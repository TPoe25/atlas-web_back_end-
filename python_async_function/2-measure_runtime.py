#!/usr/bin/env python3
import asyncio
import time
from typing import List

from _0_basic_async_syntax_ import wait_random
from _1_concurrent_coroutines_ import wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
