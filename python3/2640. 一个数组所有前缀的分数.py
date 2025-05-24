class Solution:

    def findPrefixScore(self, nums: List[int]) -> List[int]:

        pre_max = list(accumulate(nums, func=max))

        return list(accumulate([nums[i] + pre_max[i] for i in range(len(nums))]))
