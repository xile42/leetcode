class Solution:

    def maximumOr(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] | nums[i]
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] | nums[i]

        ans = -inf
        for i in range(n):
            left = 0 if i == 0 else pre[i - 1]
            right = 0 if i == n - 1 else suf[i + 1]
            ans = max(ans, left | right | (nums[i] << k))

        return ans
