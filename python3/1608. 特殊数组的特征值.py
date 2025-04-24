class Solution:

    def specialArray(self, nums: List[int]) -> int:

        nums = sorted(nums, reverse=True) + [0]
        for idx in range(len(nums) - 1):
            if nums[idx] >= idx + 1 > nums[idx + 1]:
                return idx + 1

        return -1
