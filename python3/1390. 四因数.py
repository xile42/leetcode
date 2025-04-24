class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        ans = 0
        for n in nums:
            factors = set()
            for i in range(1, isqrt(n) + 1):
                if n % i == 0:
                    factors.add(i)
                    factors.add(n // i)
                if len(factors) > 4:
                    break
            if len(factors) == 4:
                ans += sum(factors)

        return ans
