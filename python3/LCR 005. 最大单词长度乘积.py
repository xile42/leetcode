class Solution:

    def maxProduct(self, words: List[str]) -> int:

        n = len(words)
        ns = [0] * n
        for i, w in enumerate(words):
            for c in w:
                ns[i] |= 1 << (ord(c) - ord("a"))

        ans = 0
        for i, mi in enumerate(ns):
            for j, mj in enumerate(ns):
                if mi & mj:
                    continue
                ans = max(ans, len(words[i]) * len(words[j]))

        return ans
