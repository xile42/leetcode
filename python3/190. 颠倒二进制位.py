class Solution:

    def reverseBits(self, n: int) -> int:

        sn = bin(n)[2:]

        while len(sn) < 32:
            sn = "0" + sn

        return int(sn[::-1], 2)
