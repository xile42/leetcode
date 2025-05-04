class Solution:

    def hasAlternatingBits(self, n: int) -> bool:

        sn = bin(n)[2:]

        return all(sn[i] != sn[i - 1] for i in range(1, len(sn)))
