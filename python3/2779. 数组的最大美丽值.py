class Solution:

    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = left = 0
        tar = 2 * k
        
        for right, n in enumerate(nums):
            while n - nums[left] > tar:
                left += 1
            ans = max(ans, right - left + 1)

        return ans
