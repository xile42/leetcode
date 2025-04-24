class Solution:

    def findTheArrayConcVal(self, nums: List[int]) -> int:

        ans = 0
        while len(nums):

            if len(nums) == 1:
                ans += nums[0]
                nums.pop(0)
                break
            
            ans += int(str(nums[0]) + str(nums[-1]))
            nums = nums[1:-1]

        return ans
