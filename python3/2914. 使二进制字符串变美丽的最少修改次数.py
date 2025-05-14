class Solution:

    def minChanges(self, s: str) -> int:

        ns = list()
        for c, ite in groupby(s):
            l = len(list(ite))
            ns.append(l & 1)

        ans = 0
        pre = None
        for i, n in enumerate(ns):
            if n & 1:
                if pre is None:
                    pre = i
                else:
                    ans += i - pre
                    pre = None

        return ans
