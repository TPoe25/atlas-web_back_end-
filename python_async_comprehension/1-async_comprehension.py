#!/usr/bin/env python3
""" An async comprehension is a way to create a list from an async generator.
"""


import asyncio
from typing import AsyncGenerator, List


class Generator:
    async def __aiter__(self):
        for i in range(10):
            yield i
async def async_comprehension() -> List[float]:
    return [num async for num in Generator()]
