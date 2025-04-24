class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def f(goal):
            
            left = 0
            cur = 0
            cnt = 0
            for right in range(len(nums)):
                cur += nums[right]
                while cur > goal and left <= right:
                    cur -= nums[left]
                    left += 1

                cnt += (right - left + 1)
            
            return cnt

        return f(goal) - f(goal-1)
