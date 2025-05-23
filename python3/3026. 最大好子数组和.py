class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        acc = list(accumulate(nums))
        d = defaultdict(lambda: inf)
        ans = -inf
        for i, n in enumerate(nums):
            cur = acc[i]
            ans = max(ans, cur - d[n + k], cur - d[n - k])
            d[n] = min(d[n], 0 if i == 0 else acc[i - 1])

        return ans if ans > -inf else 0
