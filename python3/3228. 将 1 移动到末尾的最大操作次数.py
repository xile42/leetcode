class Solution:

    def maxOperations(self, s: str) -> int:

        ns = list()
        for c, ite in groupby(s):
            if c == "1":
                ns.append(len(list(ite)))

        ans = 0
        cur = 0
        for i in range(1, len(ns)):
            cur += ns[i - 1]
            ans += cur
        if s[-1] == "0":
            ans += sum(ns)

        return ans
