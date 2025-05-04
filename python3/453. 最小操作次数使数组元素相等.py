class Solution:

    def minMoves(self, nums: List[int]) -> int:

        mn = min(nums)

        return sum([n - mn for n in nums])
