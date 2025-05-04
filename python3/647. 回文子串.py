class Solution:

    def countSubstrings(self, s: str) -> int:

        n = len(s)
        ans = 0

        def f(i, j):

            if not (i >= 0 and j < n):
                return

            nonlocal ans
            if s[i] == s[j]:
                ans += 1
                f(i - 1, j + 1)

        for i in range(n):
            f(i, i)
            f(i, i + 1)

        return ans
