class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:

            s = set(nums)
            for i in count(1):
                if i not in s:
                    return i