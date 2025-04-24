class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        s = sum(arr)
        base = pow(10, 9) + 7

        def f(nums):
            dp = [0] * len(nums)
            for i, n in enumerate(nums):
                if i == 0:
                    dp[i] = max(nums[i], 0)
                else:
                    dp[i] = max(dp[i - 1], 0) + nums[i]

            return max(dp)

        if k == 1:
            return f(arr) % base
        else:
            return (f(arr+arr) + max(s * (k - 2), 0)) % base
