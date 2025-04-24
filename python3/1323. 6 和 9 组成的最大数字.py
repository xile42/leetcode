class Solution:

    def maximum69Number (self, num: int) -> int:

        sn = str(num)
        i = sn.find("6")
        if i == -1:
            return num

        return int(sn[:i] + "9" + sn[i + 1:])
