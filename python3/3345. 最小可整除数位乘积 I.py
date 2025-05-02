from typing import *
from functools import *
from heapq import *


class Solution:

    def smallestNumber(self, n: int, t: int) -> int:

        cur = n
        while True:
            ns = map(int, str(cur))
            p = 1
            for i in ns:
                p *= i
            if p % t == 0:
                return cur
            cur += 1