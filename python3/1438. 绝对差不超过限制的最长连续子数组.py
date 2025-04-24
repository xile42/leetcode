class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:

        ans = left = 0
        s = SortedList()
        for right in range(len(nums)):
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ans = max(ans, right - left + 1)

        return ans
