class Solution:

    def removeAlmostEqualCharacters(self, word: str) -> int:

        ans = 0
        n = len(word)
        ns = [ord(c) for c in word]
        for i in range(1, n):
            if abs(ns[i - 1] - ns[i]) <= 1:
                ns[i] = inf
                ans += 1

        return ans
