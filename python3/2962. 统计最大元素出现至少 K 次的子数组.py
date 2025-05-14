class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:

        mx = max(nums)
        ans = left = 0
        n = len(nums)
        cnt = 0
        for right in range(n):
            if nums[right] == mx:
                cnt += 1
            while cnt >= k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            if left and nums[left - 1] == mx and cnt == k - 1:
                ans += left

        return ans
