class Solution:

    def findMiddleIndex(self, nums: List[int]) -> int:

        acc = list(accumulate(nums))
        s = acc[-1]
        for idx in range(len(nums)):
            left = 0 if idx == 0 else acc[idx - 1]
            if left * 2 + nums[idx] == s:
                return idx

        return -1
