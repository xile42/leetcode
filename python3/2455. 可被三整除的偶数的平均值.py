class Solution:

    def averageValue(self, nums: List[int]) -> int:

        ns = [i for i in nums if i & 1 == 0 and i % 3 == 0]

        return 0 if len(ns) == 0 else sum(ns) // len(ns)
