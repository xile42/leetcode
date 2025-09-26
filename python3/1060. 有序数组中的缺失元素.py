class Solution:

    def missingElement(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            missing = nums[mid] - nums[0] - mid

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        return nums[0] + k + left - 1
