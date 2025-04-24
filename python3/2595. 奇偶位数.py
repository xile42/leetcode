class Solution:

    def evenOddBit(self, n: int) -> List[int]:

        sn = bin(n)[2:][::-1]
        even = sn[::2].count("1")
        odd = sn[1::2].count("1")

        return [even, odd]
