class Solution:

    def numberOfWays(self, s: str) -> int:

        n = len(s)
        ans = 0
        for tar in ["010", "101"]:
            a = b = d = 0
            for c in s:
                if c == tar[0]:
                    a += 1
                if c == tar[1]:
                    b += a
                if c == tar[2]:
                    d += b
            ans += d

        return ans
                    
