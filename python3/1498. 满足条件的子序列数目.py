class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:

        base = 10**9 + 7

        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right - left, base)
                ans %= base
                left += 1

        return ans
