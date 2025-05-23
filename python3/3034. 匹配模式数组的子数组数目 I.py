class Solution:

    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        ns = [1 if nums[i] < nums[i + 1] else (-1 if nums[i] > nums[i + 1] else 0) for i in range(len(nums) - 1)]
        ans = 0
        for i in range(len(ns) + 1 - len(pattern)):
            if ns[i:i + len(pattern)] == pattern:
                ans += 1

        return ans
