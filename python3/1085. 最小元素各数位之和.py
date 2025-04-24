class Solution:

    def sumOfDigits(self, nums: List[int]) -> int:

        return 0 if sum(map(int, str(min(nums)))) & 1 else 1
