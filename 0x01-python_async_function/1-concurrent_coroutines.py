#!/usr/bin/env python3
"""this module defines and asyncronous
ecoroutine that calls a function n times
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''wait_n calls a function n times as a routine'''
    coroutines = [wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*coroutines)
    return (result)
