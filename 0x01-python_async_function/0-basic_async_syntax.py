#!/usr/bin/env python3

"""
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10)
waits for a random delay between 0 and max_delay
 seconds and eventually returns it.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
