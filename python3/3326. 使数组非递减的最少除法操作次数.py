class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def f(n):

            for i in range(2, isqrt(n) + 1):
                if n % i == 0:
                    return n // i

            return 1

        ans = 0
        cur = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            v = nums[i]
            if v <= cur:
                cur = v
                continue
            while v > cur:
                next_v = v // f(v)
                if next_v == v and next_v > cur:
                    return -1
                v = next_v
                ans += 1
            cur = v

        return ans
