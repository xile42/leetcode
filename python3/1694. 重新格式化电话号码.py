class Solution:

    def reformatNumber(self, number: str) -> str:

        s = number.replace(" ", "").replace("-", "")
        results = list()
        d, r = divmod(len(s), 3)
        parts = list()
        if r == 1:
            if d == 0:
                return s
            else:
                d -= 1
                r += 3
                parts = [3 for _ in range(d)] + [2, 2]
        else:
            parts = [3 for _ in range(d)]
            if r != 0:
                parts += [r]

        cur = 0
        for l in parts:
            results.append(s[cur:cur+l])
            cur += l

        return "-".join(results)
