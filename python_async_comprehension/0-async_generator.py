#!/usr/bin/env python3

"""
coroutine to loop 10 times, each time asynchronously
wait 1 second then yield a random number between 0
and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10,
    waiting 1 second between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronous wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
