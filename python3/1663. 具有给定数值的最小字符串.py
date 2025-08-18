class Solution:

    def getSmallestString(self, n: int, k: int) -> str:

        ns = list()
        for _ in range(n):
            cur = 1 if k - 26 * (n - 1 - len(ns)) <= 0 else k - 26 * (n - 1 - len(ns))
            ns.append(cur)
            k -= cur

        ans = [chr(ord("a") + offset - 1) for offset in ns]

        return "".join(ans)
