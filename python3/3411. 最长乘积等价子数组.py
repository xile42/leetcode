class Solution:

    def maxLength(self, nums: List[int]) -> int:

        def lcm(a, b):
            return a * b // gcd(a, b)

        def check(ns):
            return reduce(mul, ns) == reduce(lcm, ns) * gcd(*ns)

        ans = 1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if check(nums[i:j+1]):
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
