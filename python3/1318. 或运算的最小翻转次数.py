class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:

        ans = 0
        for i in range(32):
            aa, bb, cc = a >> i & 1, b >> i & 1, c >> i & 1
            if cc:
                ans += 1 - (aa | bb)
            else:
                ans += aa + bb

        return ans