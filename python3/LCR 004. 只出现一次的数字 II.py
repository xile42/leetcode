class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for idx in range(32):
            bit_sum = sum([(num >> idx) & 1 for num in nums])

            if bit_sum % 3 != 0:
                if idx == 31:
                    result -= 1 << idx
                else:
                    result |= 1 << idx

        return result
