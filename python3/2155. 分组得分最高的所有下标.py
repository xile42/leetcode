class Solution:

    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre = [0] * n
        pre[0] = (nums[0] == 0)
        for i in range(1, n):
            pre[i] = pre[i - 1] + (nums[i] == 0)

        suf = [0] * n
        suf[n - 1] = (nums[n - 1] == 1)
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + (nums[i] == 1)

        ns = [0] * (n + 1)
        for i in range(n + 1):
            cur = (0 if i == 0 else pre[i - 1]) + (0 if i == n else suf[i])
            ns[i] = cur

        mx = max(ns)
        ans = [i for i in range(n + 1) if ns[i] == mx]

        return ans
