class Solution:

    def findLatestTime(self, s: str) -> str:

        a, b, _, c, d = s
        ans = str()
        ans += ("1" if b == "?" or b <= "1" else "0") if a == "?" else a
        ans += ("1" if ans[-1] == "1" else "9") if b == "?" else b
        ans += ":"
        ans += "5" if c == "?" else c
        ans += "9" if d == "?" else d

        return ans
