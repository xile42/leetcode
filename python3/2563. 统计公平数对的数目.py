class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, n in enumerate(nums):
            r = bisect_right(nums, upper - n, i + 1, len(nums))
            l = bisect_left(nums, lower - n, i + 1, len(nums))
            ans += r - l

        return ans
