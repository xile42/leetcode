class Solution:

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0
        i = 0
        for x in nums[(len(nums) + 1) // 2:]:
            if x >= 2 * nums[i]:
                i += 1
                ans += 2

        return ans
