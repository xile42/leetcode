class Solution:

    def maximumSumScore(self, nums: List[int]) -> int:

        return max(max(list(accumulate(nums))), max(list(accumulate(nums[::-1]))))
