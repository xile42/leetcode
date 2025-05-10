class Solution:

    def numberOfSteps(self, num: int) -> int:

        l = num.bit_length()
        c = num.bit_count()

        return l + c - 1 if num > 0 else 0