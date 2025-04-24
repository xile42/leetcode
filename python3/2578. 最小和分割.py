class Solution:

    def splitNum(self, num: int) -> int:

        sn = sorted(str(num))

        return int("".join(sn[::2])) + int("".join(sn[1::2]))
