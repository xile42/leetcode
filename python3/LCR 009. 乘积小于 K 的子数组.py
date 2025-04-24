class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        ans = left = 0
        cur = 1
        n = len(nums)
        for right in range(n):
            cur *= nums[right]
            while cur >= k:
                cur //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
