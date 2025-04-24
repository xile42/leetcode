class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:

        ns = list(Counter(nums).values())

        return sum([n for n in ns if n == max(ns)])
