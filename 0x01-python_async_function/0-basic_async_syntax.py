#!/usr/bin/env python3
"""this module defines and asyncronous coroutine that takes in an integer"""
import asyncio
from typing import Awaitable
import random


async def wait_random(max_delay: int = 10) -> Awaitable[float]:
    """ asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    """
    interval = random.uniform(0, max_delay)
    x = await asyncio.sleep(interval)
    return (interval)
