class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        sn = sorted(nums)
        idx = 0
        for _ in range(len(nums) - k):
            nums.pop(nums.index(sn[idx]))
            idx += 1

        return nums
