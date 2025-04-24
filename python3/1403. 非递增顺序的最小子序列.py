class Solution:

    def minSubsequence(self, nums: List[int]) -> List[int]:

        tar = sum(nums) / 2
        nums = sorted(nums, reverse=True)
        ans = list()
        t = 0
        idx = 0
        while t <= tar:
            t += nums[idx]
            ans.append(nums[idx])
            idx += 1

        return ans
