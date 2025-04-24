class Solution:

    def maximumCount(self, nums: List[int]) -> int:

        if nums[-1] < 0 or nums[0] > 0:
            return len(nums)

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] >= 0:
                right = mid-1
            else:
                left = mid+1
        neg_count = left

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] <= 0:
                left = mid+1
            else:
                right = mid-1
        pos_count = len(nums)-left

        return max(neg_count, pos_count)
