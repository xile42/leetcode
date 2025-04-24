class Solution:

    def similarPairs(self, words: List[str]) -> int:

        c = Counter([tuple(sorted(Counter(w).keys())) for w in words])
        ans = 0
        for v in c.values():
            if v > 1:
                ans += v * (v - 1) // 2

        return ans
