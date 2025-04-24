class Solution:

    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        m = 1
        while m <= n:
            if m == n:
                return True
            m *= 3

        return False
