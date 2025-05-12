class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = [""] * (len(s) + len(spaces))
        for idx, i in enumerate(spaces):
            ans[i + idx] = " "

        i = 0
        for j, c in enumerate(ans):
            if c == "":
                ans[j] = s[i]
                i += 1

        return "".join(ans)
