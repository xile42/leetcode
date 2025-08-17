class Solution:

    def encode(self, num: int) -> str:

        if num <= 6:
            return ["", "0", "1", "00", "01", "10", "11"][num]

        l = (num + 2).bit_length() - 1
        offset = num - (1 << l) + 2 - 1
        ans = bin(offset)[2:][-l:]
        ans = ans.zfill(l)

        return ans
