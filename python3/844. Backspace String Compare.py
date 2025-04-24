class Solution:

    def parse(self, s):

        result = list()
        for char in s:
            if char == "#":
                if len(result) > 0:
                    result.pop(-1)
            else:
                result.append(char)

        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:

        return self.parse(s) == self.parse(t)
