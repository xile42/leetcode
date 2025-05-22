class Solution:

    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x > 1

        ans = 0
        pre = None
        for i, x in enumerate(nums):
            if is_prime(x):
                if pre is None:
                    pre = i
                else:
                    ans = max(ans, i - pre)

        return ans
