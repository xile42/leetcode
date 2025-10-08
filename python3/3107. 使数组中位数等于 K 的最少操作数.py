class Solution:

    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()
        ans = 0
        mid = n // 2

        for i in range(mid):
            if nums[i] > k:
                ans += nums[i] - k
        for i in range(mid + 1, n):
            if nums[i] < k:
                ans += k - nums[i]
        ans += abs(nums[mid] - k)

        return ans
