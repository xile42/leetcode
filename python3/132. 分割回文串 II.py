class Solution:

    def minCut(self, s: str) -> int:

        n = len(s)

        @cache
        def is_huiwen(i, j):

            if i >= j:
                return True

            return s[i] == s[j] and is_huiwen(i + 1, j - 1)

        @cache
        def f(i):

            if i >= n:
                return 0

            if is_huiwen(i, n - 1):
                return 1

            ans = inf
            for j in range(i, n - 1):
                if is_huiwen(i, j):
                    ans = min(ans, 1 + f(j + 1))

            return ans

        ans = f(0)

        return ans - 1
