class Solution:

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diffs = [abs(nums[i] - nums[i - 1]) for i in range(1, len(nums))]
        diffs.append(abs(nums[0] - nums[-1]))

        return max(diffs)