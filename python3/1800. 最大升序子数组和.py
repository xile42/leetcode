class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:

        idxs = [0] + [idx for idx in range(1, len(nums)) if nums[idx] <= nums[idx - 1]] + [len(nums)]
        ans = 0
        for i, j in pairwise(idxs):
            ans = max(ans, sum(nums[i:j]))

        return ans
