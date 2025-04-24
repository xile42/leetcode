class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        ans = 0
        for i in sorted(set(range(1, n + 1)) - set(banned)):
            if i <= maxSum:
                maxSum -= i
                ans += 1

        return ans
