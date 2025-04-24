class Solution:

    def checkString(self, s: str) -> bool:

        i = s.find("b")
        if i == -1:
            return True

        return "a" not in s[i:]
