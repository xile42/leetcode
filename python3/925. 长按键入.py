class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:

        s1 = str()
        c1 = [1] * max(len(name), len(typed))
        s2 = str()
        c2 = [1] * max(len(name), len(typed))
        for char in name:
            if not s1 or char != s1[-1]:
                s1 += char
            elif char == s1[-1]:
                c1[len(s1) - 1] += 1
        for char in typed:
            if not s2 or char != s2[-1]:
                s2 += char
            elif char == s2[-1]:
                c2[len(s2) - 1] += 1

        return s1 == s2 and all(c2[i] >= c1[i] for i in range(len(c1)))
