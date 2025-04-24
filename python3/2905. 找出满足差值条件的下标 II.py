class Solution:

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        mx_idx, mn_idx = None, None
        for j in range(indexDifference, len(nums)):
            cur_idx = j - indexDifference
            cur = nums[cur_idx]

            mx_idx = cur_idx if mx_idx is None or nums[mx_idx] < cur else mx_idx
            mn_idx = cur_idx if mn_idx is None or nums[mn_idx] > cur else mn_idx

            if mx_idx is not None and nums[j] <= nums[mx_idx] - valueDifference:
                return [mx_idx, j]
            if mn_idx is not None and nums[j] >= valueDifference + nums[mn_idx]:
                return [mn_idx, j]

        return [-1, -1]
