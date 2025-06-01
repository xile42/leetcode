class Solution:

    def maxValue(self, n: str, x: int) -> str:

        s = list(n)
        x = str(x)
        if s[0] != "-":
            for i, c in enumerate(s):
                if c < x:
                    s.insert(i, x)
                    return "".join(s)
        else:
            for i, c in enumerate(s):
                if i == 0:
                    continue
                if c > x:
                    s.insert(i, x)
                    return "".join(s)

        s.append(x)
        return "".join(s)
