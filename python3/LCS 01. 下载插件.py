class Solution:

    def leastMinutes(self, n: int) -> int:

        v = 1
        ans = 0
        while ceil(n / v) - ceil(n / (v * 2)) > 1:
            v *= 2
            ans += 1

        return ans + ceil(n / v)
