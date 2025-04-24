class Solution:

    def maximumDifference(self, nums: List[int]) -> int:

        ans = -inf
        cur = inf
        for n in nums:
            if n > cur:
                ans = max(ans, n - cur)
            cur = min(cur, n)

        return ans if ans > -inf else -1
