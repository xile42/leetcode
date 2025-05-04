class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        choices = [[s.count("0"), s.count("1")] for s in strs]

        @cache
        def f(cur, m, n):

            if m < 0 or n < 0:
                return -inf

            if cur >= len(choices):
                return 0

            ans = -inf
            vm, vn = choices[cur]
            for i in range(2):
                ans = max(ans, f(cur + 1, m - i * vm, n - i * vn) + i)

            return ans

        ans = f(0, m, n)
        f.cache_clear()

        return ans
