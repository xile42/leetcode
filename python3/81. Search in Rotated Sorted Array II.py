# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
#
#  Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1]
# , ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0
# ,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,
# 2,4,4].
#
#  Given the array nums after the rotation and an integer target, return true
# if target is in nums, or false if it is not in nums.
#
#  You must decrease the overall operation steps as much as possible.
#
#
#  Example 1:
#  Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#  Example 2:
#  Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 5000
#  -10⁴ <= nums[i] <= 10⁴
#  nums is guaranteed to be rotated at some pivot.
#  -10⁴ <= target <= 10⁴
#
#
#
#  Follow up: This problem is similar to Search in Rotated Sorted Array, but
# nums may contain duplicates. Would this affect the runtime complexity? How and why?
#
#
#  Related Topics Array Binary Search 👍 8577 👎 1051


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:  # 左侧连续
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右侧连续
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# leetcode submit region end(Prohibit modification and deletion)
