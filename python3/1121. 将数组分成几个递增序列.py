class Solution:

    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:

        c = Counter(nums)

        return max(c.values()) <= len(nums) // k
