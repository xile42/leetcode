class Solution:

    def alternatingSum(self, nums: List[int]) -> int:

        a = sum(n for i, n in enumerate(nums) if i % 2 == 0)
        b = sum(n for i, n in enumerate(nums) if i % 2 == 1)

        return a - b
