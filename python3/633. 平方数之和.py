class Solution:

    def judgeSquareSum(self, c: int) -> bool:

        ns = set()
        i = 0
        while (t := i * i) <= c:
            ns.add(t)
            i += 1

        for i in ns:
            if c - i in ns:
                return True

        return False
