class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:

        @cache
        def f(cur, tar):

            if tar < 0:
                return -inf

            if cur >= len(stones):
                return 0

            ans = 0
            for i in range(2):
                ans = max(ans, f(cur + 1, tar - i * stones[cur]) + i * stones[cur])

            return ans

        ans = f(0, int(sum(stones) / 2))
        f.cache_clear()

        return sum(stones) - 2 * ans
