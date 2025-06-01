class Solution:

    def minFlips(self, target: str) -> int:

        ans = 0
        cs = ["0", "1"]
        idx = 0
        for c in target:
            if c != cs[idx]:
                ans += 1
                idx = 1 - idx

        return ans
