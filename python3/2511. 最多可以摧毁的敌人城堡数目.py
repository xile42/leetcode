class Solution:

    def captureForts(self, forts: List[int]) -> int:

        ns = list()
        for c, ite in groupby(forts):
            ns.append([c, len(list(ite))])

        ans = 0
        for i, (n, l) in enumerate(ns):
            if i == 0 or i == len(ns) - 1:
                continue
            if n != 0:
                continue
            if (ns[i - 1][0] == 1 and ns[i + 1][0] == -1) or (ns[i - 1][0] == -1 and ns[i + 1][0] == 1):
                ans = max(ans, l)

        return ans
