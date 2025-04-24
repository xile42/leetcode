class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        s = set(nums)

        return sum(x - diff in s and x + diff in s for x in nums)
