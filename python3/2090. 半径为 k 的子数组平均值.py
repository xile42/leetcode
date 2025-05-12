class Solution:

    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        ans = [-1] * n
        k = 2 * k + 1
        s = 0
        for i, v in enumerate(nums):
            s += v
            if i >= k:
                s -= nums[i - k]
            if i >= k - 1:
                ans[i - (k - 1) // 2] = s // k

        return ans
