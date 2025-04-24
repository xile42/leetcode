class Solution:

    def countPartitions(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 1 - 1, -1, -1):
            suf[i] = suf[i + 1] + nums[i]

        for i in range(n - 1):
            left = pre[i]
            right = suf[i + 1]
            if abs(left - right) & 1 == 0:
                ans += 1

        return ans
