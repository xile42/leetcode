class Solution:

    def alternatingSubarray(self, nums: List[int]) -> int:

        ans = -1
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            start = i
            i += 2
            while i < n and (nums[i] - nums[i - 1]) * (nums[i - 1] - nums[i - 2]) == -1:
                i += 1
            ans = max(ans, i - start)
            i -= 1

        return ans
