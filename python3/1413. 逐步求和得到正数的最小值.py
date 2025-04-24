class Solution:

    def minStartValue(self, nums: List[int]) -> int:

        v = min(accumulate(nums))

        return 1 if v >= 0 else abs(v) + 1
