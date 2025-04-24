class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = dict()
        for i in range(len(nums)):
            v = nums[i]
            if v in d and i - d[v] <= k:
                return True
            d[v] = i

        return False
