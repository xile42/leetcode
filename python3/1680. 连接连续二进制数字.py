class Solution:

    def concatenatedBinary(self, n: int) -> int:

        cur = 0
        base = 10 ** 9 + 7
        for i in range(1, n + 1):
            cur = ((cur << i.bit_length()) + i) % base

        return cur
