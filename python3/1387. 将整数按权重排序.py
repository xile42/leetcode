class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        @cache
        def f(n):

            if n == 1:
                return 0

            if n & 1:
                return 1 + f(n * 3 + 1)
            else:
                return 1 + f(n // 2)

        ns = list()
        for n in range(lo, hi + 1):
            ns.append([f(n), n])

        ns.sort()

        return ns[k - 1][1]
