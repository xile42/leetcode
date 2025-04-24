class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:

        return int(sum([(i - 1) * i / 2 for i in Counter(nums).values()]))
