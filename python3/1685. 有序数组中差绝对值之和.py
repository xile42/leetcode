class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = nums[i] + pre[i - 1]
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i] + suf[i + 1]

        ans = list()
        for i, num in enumerate(nums):
            left = 0 if i == 0 else pre[i - 1]
            right = 0 if i == n - 1 else suf[i + 1]
            ans.append(-left + right + (2 * i - n + 1) * num)

        return ans
