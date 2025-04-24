class Solution:

    def minOperations(self, nums: List[int]) -> int:

        result = 0
        for idx in range(len(nums) - 2):
            if nums[idx] == 0:
                nums[idx + 1] ^= 1
                nums[idx + 2] ^= 1
                result += 1

        return result if nums[-1] == 1 and nums[-2] == 1 else -1
