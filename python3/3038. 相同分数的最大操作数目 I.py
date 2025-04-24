class Solution:

    def maxOperations(self, nums: List[int]) -> int:

        vs = [sum(nums[i * 2:(i+1) * 2]) for i in range(len(nums) // 2)]

        for i, ite in groupby(vs):
            return len(list(ite))
