class Solution:

    def minimumSum(self, nums: List[int]) -> int:

        n = len(nums)
        pre = [inf] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = min(pre[i - 1], nums[i])
        suf = [inf] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        ans = inf
        for i in range(1, n - 1):
            mid = nums[i]
            if mid > pre[i - 1] and mid > suf[i + 1]:
                ans = min(ans, mid + pre[i - 1] + suf[i + 1])

        return ans if ans < inf else -1
