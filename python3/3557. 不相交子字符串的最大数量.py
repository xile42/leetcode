class Solution:

    def maxSubstrings(self, word: str) -> int:

        ans = 0
        d = dict()
        for right, c in enumerate(word):
            if c in d and right - d[c] + 1 >= 4:
                ans += 1
                d = dict()
            elif c not in d:
                d[c] = right

        return ans
