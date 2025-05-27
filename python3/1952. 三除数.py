class Solution:

    def isThree(self, n: int) -> bool:

        ans = 0
        k = isqrt(n)
        if k * k != n or n == 1:
            return False
        for i in range(2, k):
            if n % i == 0:
                ans += 1

        return ans == 0
