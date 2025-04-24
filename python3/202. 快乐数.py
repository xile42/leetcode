class Solution:

    def isHappy(self, n: int) -> bool:

        visit = set()
        visit.add(n)
        while n != 1:
            ds = map(int, list(str(n)))
            n = sum([i ** 2 for i in ds])
            if n in visit:
                return False
            visit.add(n)

        return True
