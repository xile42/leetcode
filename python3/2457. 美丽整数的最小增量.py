class Solution:

    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        ns = list(map(int, str(n)))
        if sum(ns) <= target:
            return 0

        pre = n
        cnt = 0
        while True:
            cnt += 1
            n //= 10
            n += 1
            ns = list(map(int, str(n)))
            cur = sum(ns)
            if cur <= target and n * 10 ** cnt > pre:
                return n * 10 ** cnt - pre
