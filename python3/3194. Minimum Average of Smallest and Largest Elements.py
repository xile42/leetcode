class Solution:

    def minimumAverage(self, nums: List[int]) -> float:

        nums = sorted(nums)
        min_value = float("inf")
        for _ in range(len(nums) // 2):
            min_value = min(min_value, (nums[0] + nums[-1]) / 2)
            nums = nums[1:-1]

        return min_value
