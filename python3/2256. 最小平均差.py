class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:

        n = len(nums)
        pre = [0] * n
        for i, v in enumerate(nums):
            pre[i] = pre[i - 1] + v if i else v
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + nums[i] if i < n - 1 else nums[i]

        ans = None
        mn = inf
        for i in range(n):
            if i == n - 1:
                avg = pre[i] // (i + 1)
            else:
                avg = abs(pre[i] // (i + 1) - suf[i + 1] // (n - i - 1))

            if avg < mn:
                mn = avg
                ans = i

        return ans
