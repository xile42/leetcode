class Solution:

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        mx = -inf
        mx_idx = None
        mn = inf
        mn_idx = None
        for i in range(indexDifference, len(nums)):
            right = nums[i]
            left = nums[i - indexDifference]
            if left > mx:
                mx = left
                mx_idx = i - indexDifference
            if left < mn:
                mn = left
                mn_idx = i - indexDifference
            if abs(right - mx) >= valueDifference:
                return [mx_idx, i]
            if abs(right - mn) >= valueDifference:
                return [mn_idx, i]

        return [-1, -1]
