class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:

        ans = left = 0
        cur = 0
        for right in range(len(nums)):
            if right > left:
                cur += cur // (right - left)
            cur += nums[right] * (right - left + 1)
            while cur >= k:
                cur -= nums[left] * (right - left + 1)
                cur -= cur // (right - left + 1)
                left += 1
            ans += right - left + 1

        return ans
