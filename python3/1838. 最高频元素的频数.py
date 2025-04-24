class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = left = 0
        cur = 0
        last = None
        for right, n in enumerate(nums):
            cur += (n - last) * (right - left) if last else 0
            while cur > k:
                cur -= n - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            last = n

        return ans
