class Solution:

    def differenceOfSum(self, nums: List[int]) -> int:

        a = sum(nums)
        b = sum(sum(list(map(int, str(n))))for n in nums)

        return abs(a - b)
