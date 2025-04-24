class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        return sum(1 if n % 3 != 0 else 0 for n in nums)
