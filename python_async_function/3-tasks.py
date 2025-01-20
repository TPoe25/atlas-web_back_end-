#!/usr/bin/env python3
""" makes function task_wait_random that returns a asyncio.Task
"""


import asyncio
import importlib
wait_random = getattr(importlib.import_module("0-basic_async_syntax"),
                      "wait_random")


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ gets int max_delay and returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
