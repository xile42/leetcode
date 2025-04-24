class Solution:

    def fraction(self, cont: List[int]) -> List[int]:

        m, n = 0, 1
        for i in cont[::-1]:
            m += n * i
            m, n = n, m

        v = gcd(m, n)

        return [n // v, m // v]
