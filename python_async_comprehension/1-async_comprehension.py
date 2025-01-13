#!/usr/bin/env python3
from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    return[num async for num in async_generator()]
