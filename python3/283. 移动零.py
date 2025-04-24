class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i, x in enumerate(nums):
            if x == 0:
                for j in range(i + 1, n):
                    y = nums[j]
                    if y != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

