class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:

        ans = 0
        for i in range(max(0, n - 2 * limit), min(limit, n) + 1):
            j_range = min(n - i, limit) - max(0, n - i - limit) + 1
            ans += j_range

        return ans