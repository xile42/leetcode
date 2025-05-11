class Solution:

    def findTheWinner(self, n: int, k: int) -> int:

        ns = list(range(1, n + 1))
        i = 0
        for _ in range(n - 1):
            cur = (i + (k - 1)) % len(ns)
            ns.pop(cur)
            if cur == len(ns):
                cur = 0
            i = cur

        return ns[0]
