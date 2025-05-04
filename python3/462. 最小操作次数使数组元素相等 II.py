class Solution:

    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()
        tar = nums[(len(nums) - 1) // 2]

        return sum(abs(v - tar) for v in nums)
