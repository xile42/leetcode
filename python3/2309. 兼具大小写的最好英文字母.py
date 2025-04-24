class Solution:

    def greatestLetter(self, s: str) -> str:

        for c in string.ascii_uppercase[::-1]:
            if c in s and c.lower() in s:
                return c

        return str()
