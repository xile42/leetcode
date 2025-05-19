class Solution:

    def valueAfterKSeconds(self, n: int, k: int) -> int:

        base = 10 ** 9 + 7
        ns = [1] * n
        for _ in range(k):
            ns = list(accumulate(ns))
            if ns[-1] > base:
                ns = [i % base for i in ns]

        return ns[-1] % base
