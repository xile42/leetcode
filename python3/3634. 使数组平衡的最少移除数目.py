class Solution:

    def minRemoval(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        ans = inf
        for i, v in enumerate(nums):
            j = bisect_right(nums, v * k)
            ans = min(ans, n - (j - i))

        return ans
