class Solution:

    def numberOfSubstrings(self, s: str) -> int:

        c = Counter(s)
        ans = 0
        for v in c.values():
            ans += v * (v + 1) // 2

        return ans
