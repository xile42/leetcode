class Solution:

    def finalString(self, s: str) -> str:

        ans = str()
        for c in s:
            if c == "i":
                ans = ans[::-1]
            else:
                ans += c

        return ans
