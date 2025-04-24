class Solution:

    def reformat(self, s: str) -> str:

        ds, cs = [], []
        for c in s:
            if c.isalpha():
                cs.append(c)
            else:
                ds.append(c)

        if abs(len(ds) - len(cs)) > 1:
            return ""

        l1, l2 = len(ds), len(cs)
        l = min(l1, l2)
        if l1 >= l2:
            result = "".join([ds[i]+cs[i] for i in range(l)]) + "".join(ds[l:])
        else:
            result = "".join([cs[i]+ds[i] for i in range(l)]) + "".join(cs[l:])

        return result
