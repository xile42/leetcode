class Solution:

    def smallestPalindrome(self, s: str) -> str:

        n = len(s)

        if n == 1:
            return s

        cs = "".join(sorted(list(s[:n // 2])))
        rcs = cs[::-1]

        if n & 1:
            return cs + s[n // 2] + rcs
        else:
            return cs + rcs
