#!/usr/bin/env python3

"""
multiple coroutines at the same time with async
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async
    spawns task_wait_random n times with the specified max_delay
    return the list of all the delays (float values) in ascending order
    """
    tasks = [asyncio.create_task(task_wait_random(max_delay))
             for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
