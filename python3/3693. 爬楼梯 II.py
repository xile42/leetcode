class Solution:

    def climbStairs(self, n: int, costs: List[int]) -> int:

        @cache
        def f(i):

            if i == n:
                return 0

            ans = inf
            for offset in range(1, 4):
                j = i + offset
                if j > n:
                    continue
                this_ans = costs[j - 1] + (offset ** 2) + f(j)
                ans = min(ans, this_ans)

            return ans

        ans = f(0)
        f.cache_clear()

        return ans
