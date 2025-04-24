class Solution:

    def minOperations(self, nums: List[int]) -> int:

        mask = 0
        count = 0
        for num in nums:
            if num ^ mask == 0:
                mask = 1 - mask
                count += 1

        return count
