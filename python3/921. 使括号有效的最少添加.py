class Solution:

    def minAddToMakeValid(self, s: str) -> int:

        cur = ans = 0
        for c in s:
            if c == ")":
                if cur == 0:
                    ans += 1
                else:
                    cur -= 1
            else:
                cur += 1

        return cur + ans
