class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def f(i, j):

            if i == j:
                return 1

            if i > j:
                return 0

            if s[i] == s[j]:
                return 2 + f(i + 1, j - 1)

            return max(f(i + 1, j), f(i, j - 1))

        return f(0, len(s) - 1)
