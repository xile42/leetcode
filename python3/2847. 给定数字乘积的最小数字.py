class Solution:

    def smallestNumber(self, n: int) -> str:

        if n == 1:
            return "1"

        ns = list()
        for d in range(9, 1, -1):
            while n % d == 0:
                n //= d
                ns.append(d)

        if n != 1:
            return "-1"

        return "".join(map(str, ns[::-1]))
