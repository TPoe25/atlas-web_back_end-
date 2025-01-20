#!/usr/bin/env python3
""" An async comprehension is a way to create a list from an async generator.
"""


import asyncio
import importlib
from typing import List
async_generator = getattr(importlib.import_module("0-async_generator"),
                          "async_generator")


async def async_comprehension() -> List[float]:
    """An async comprehension that generates 10 random numbers 0 and 10"""
    result = [num async for num in async_generator()]
    return result
