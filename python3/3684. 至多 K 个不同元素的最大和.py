class Solution:

    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        ns = sorted(set(nums), reverse=True)

        return ns[:k]
