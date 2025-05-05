class Solution:

    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        ns = nums + nums
        acc = list(accumulate(ns))
        ans = 0
        for i, v in enumerate(nums):
            ans += i * v

        cur = ans
        for i in range(n - 1):
            right = n + i
            left = i
            cur += ns[right] * (n - 1)
            cur -= acc[right - 1] - acc[left]
            ans = max(ans, cur)
            ans = max(ans, cur)

        return ans
