class Solution:

    def findNthDigit(self, n: int) -> int:

        if n <= 9:
            return n

        l = 1
        cur = 9
        amount = 9
        last_cur = 0
        while cur < n:
            l += 1
            amount *= 10
            last_cur = cur
            cur += amount * l

        start = 10 ** (l - 1)
        n -= last_cur
        i = n // l
        r = n % l
        num = start + i + (-1 if r == 0 else 0)

        return int(str(num)[-1]) if r == 0 else int(str(num)[r - 1])
