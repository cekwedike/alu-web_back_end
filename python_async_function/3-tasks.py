#!/usr/bin/env python3

"""
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer
max_delay and returns a asyncio.
"""


import asyncio


# imported wait_random form the first task we did
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random coroutine

    Args:
        max_delay: maximum delay in seconds
    Returns:
        asyncio.Task Object
    """

    return asyncio.create_task(wait_random(max_delay))
