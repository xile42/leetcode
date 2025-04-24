class Solution:

    def findPeakElement(self, nums: List[int]) -> int:

        nums = [-inf] + nums + [-inf]
        n = len(nums)
        left = 1
        right = n - 2
        while left <= right:
            mid = (right + left) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1