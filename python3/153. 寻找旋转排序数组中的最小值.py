class Solution:

    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        left_most = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            v = nums[mid]
            if (mid == 0 or nums[mid - 1] > v) and (mid == len(nums) - 1 or nums[mid + 1] > v):
                return v
            if v < left_most:
                right = mid - 1
            else:
                left = mid + 1

        return nums[left]
