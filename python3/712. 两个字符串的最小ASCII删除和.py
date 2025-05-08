class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m, n = len(s1), len(s2)

        @cache
        def f(i, j):

            if i >= m or j >= n:
                return 0

            if s1[i] == s2[j]:
                return ord(s1[i]) + f(i + 1, j + 1)

            return max(f(i + 1, j), f(i, j + 1))

        v = f(0, 0)
        f.cache_clear()

        return sum([ord(c) for c in s1 + s2]) - 2 * v
