#!/usr/bin/env python3

"""
Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
"""


import asyncio
from typing import List

# import task_wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function creates a list of wait_random caroutines and uses
    asyncio.as_completed to ensure the results are obtained in ascending order.
    The resulting delays are collected in the 'delays' list and returned
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
