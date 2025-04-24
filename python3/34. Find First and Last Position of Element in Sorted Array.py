class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        idx1 = bisect_left(nums, target)
        idx2 = bisect_right(nums, target)

        if idx1 >= len(nums) or nums[idx1] != target:
            return [-1, -1]

        return [idx1, idx2 - 1]


### Given an array of integers nums sorted in non-decreasing order, find the
### starting and ending position of a given target value.
###
###  If target is not found in the array, return [-1, -1].
###
###  You must write an algorithm with O(log n) runtime complexity.
###
###
###  Example 1:
###  Input: nums = [5,7,7,8,8,10], target = 8
### Output: [3,4]
###
###  Example 2:
###  Input: nums = [5,7,7,8,8,10], target = 6
### Output: [-1,-1]
###
###  Example 3:
###  Input: nums = [], target = 0
### Output: [-1,-1]
###
###
###  Constraints:
###
###
###  0 <= nums.length <= 10⁵
###  -10⁹ <= nums[i] <= 10⁹
###  nums is a non-decreasing array.
###  -10⁹ <= target <= 10⁹
###
###
###  Related Topics Array Binary Search 👍 20617 👎 528
##
##
### leetcode submit region begin(Prohibit modification and deletion)
##class Solution:
##
##    def searchRange(self, nums: List[int], target: int) -> List[int]:
##
##        start_idx = -1
##        end_idx = -1
##
##        if len(nums) == 0:
##            return [start_idx, end_idx]
##
##        if nums[0] == target:
##            start_idx = 0
##        else:
##            left = 0
##            right = len(nums) - 1
##            while left <= right:
##                mid = left + (right - left) // 2
##                if nums[mid] == target:
##                    if mid == 0 or nums[mid-1] != target:
##                        start_idx = mid
##                        break
##                    else:
##                        right = mid - 1
##                elif nums[mid] < target:
##                    left = mid + 1
##                else:
##                    right = mid - 1
##
##        if nums[-1] == target:
##            end_idx = len(nums) - 1
##        else:
##            left = 0
##            right = len(nums) - 1
##            while left <= right:
##                mid = left + (right - left) // 2
##                if nums[mid] == target:
##                    if mid == len(nums) - 1 or nums[mid+1] != target:
##                        end_idx = mid
##                        break
##                    else:
##                        left = mid + 1
##                elif nums[mid] < target:
##                    left = mid + 1
##                else:
##                    right = mid - 1
##
##        return [start_idx, end_idx]
##
### leetcode submit region end(Prohibit modification and deletion)
