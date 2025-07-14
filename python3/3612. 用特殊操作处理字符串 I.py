class Solution:

    def processStr(self, s: str) -> str:

        ans = list()
        valid = set(string.ascii_lowercase)

        for c in s:
            if c in valid:
                ans.append(c)
            elif c == "*":
                if ans:
                    ans.pop()
            elif c == "#":
                ans += ans
            else:
                ans = ans[::-1]

        return "".join(ans)
