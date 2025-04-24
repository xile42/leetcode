class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        result = [-1] * (len(nums) - k + 1)
        cnt = 0
        for idx in range(len(nums)):
            cnt = cnt + 1 if idx == 0 or nums[idx] == nums[idx-1] + 1 else 1
            if cnt >= k:
                result[idx - k + 1] = nums[idx]

        return result