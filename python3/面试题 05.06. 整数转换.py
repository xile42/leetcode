class Solution:

    def convertInteger(self, A: int, B: int) -> int:

        return ((A & 0xffffffff) ^ (B & 0xffffffff)).bit_count()
