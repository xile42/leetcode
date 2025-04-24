class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:

        b_nums = [bin(num)[2:][::-1] for num in nums]
        b_k = bin(k)[2:][::-1]
        result = 0

        bit_odd = [0 for _ in range(20)]
        for num in b_nums:
            for idx, bit in enumerate(num):
                if bit == "1":
                    bit_odd[idx] = 1 - bit_odd[idx]

        for idx, bit in enumerate(bit_odd):
            bit = str(bit)
            if idx >= len(b_k) and bit == "1":
                result += 1
            elif idx < len(b_k) and b_k[idx] != bit:
                result += 1

        return result
