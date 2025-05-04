class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        @cache
        def f(i, j):

            if i >= m or j >= n:
                return 0

            if word1[i] == word2[j]:
                return f(i + 1, j + 1) + 1

            return max(f(i + 1, j), f(i, j + 1))

        l = f(0, 0)

        return m + n - 2 * l
