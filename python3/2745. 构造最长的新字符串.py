class Solution:

    def longestString(self, x: int, y: int, z: int) -> int:

        @cache
        def f(i, j, k, s):

            if any(v < 0 for v in [i, j, k]):
                return -inf

            if sum([i, j, k]) == 0:
                return 0

            ans = 0
            if s == 0:
                ans = max(ans, f(i, j - 1, k, 1) + 1)
            elif s == 1:
                ans = max(ans, f(i - 1, j, k, 0) + 1)
                ans = max(ans, f(i, j, k - 1, 2) + 1)
            else:
                ans = max(ans, f(i - 1, j, k, 0) + 1)
                ans = max(ans, f(i, j, k - 1, 2) + 1)

            return ans

        f.cache_clear()
        ans = max(0, f(x - 1, y, z, 0) + 1, f(x, y - 1, z, 1) + 1, f(x, y, z - 1, 2) + 1)

        return ans * 2
