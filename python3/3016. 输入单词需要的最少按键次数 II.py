class Solution:

    def minimumPushes(self, word: str) -> int:

        c = Counter(word)
        ns = sorted(c.values(), reverse=True)
        ans = sum([(i // 8 + 1) * n for i, n in enumerate(ns)])

        return ans
