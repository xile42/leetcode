class Solution:

    def minimumSum(self, nums: List[int]) -> int:

        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = min(nums[i], pre[i - 1])
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])

        ans = inf
        for i in range(1, n - 1):
            if pre[i - 1] < nums[i] and nums[i] > suf[i + 1]:
                ans = min(ans, pre[i - 1] + nums[i] + suf[i + 1])

        return ans if ans < inf else -1
