class Solution:

    def removeDuplicates(self, s: str) -> str:

        r = list()
        for char in s:
            if len(r) != 0 and char == r[-1]:
                r.pop(-1)
            else:
                r.append(char)

        return "".join(r)
