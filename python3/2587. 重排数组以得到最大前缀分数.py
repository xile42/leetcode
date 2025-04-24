class Solution:

    def maxScore(self, nums: List[int]) -> int:

        ps = [i for i in nums if i > 0]
        ns = sorted([i for i in nums if i <= 0], reverse=True)
        ns = ps + ns
        acc = list(accumulate(ns))
        ans = len([i for i in acc if i > 0])

        return ans
