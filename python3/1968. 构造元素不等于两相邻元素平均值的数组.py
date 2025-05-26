class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:

        import numpy as np

        while True:
            np.random.shuffle(nums)
            for i in range(1, len(nums) - 1):
                if nums[i] == (nums[i + 1] + nums[i - 1]) / 2:
                    break
            else:
                return nums
