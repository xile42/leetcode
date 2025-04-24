# Given an array nums with n objects colored red, white, or blue, sort them in-
# place so that objects of the same color are adjacent, with the colors in the
# order red, white, and blue.
#
#  We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
#
#  You must solve this problem without using the library's sort function.
#
#
#  Example 1:
#
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
#
#  Example 2:
#
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
#
#  Constraints:
#
#
#  n == nums.length
#  1 <= n <= 300
#  nums[i] is either 0, 1, or 2.
#
#
#
#  Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
#
#  Related Topics Array Two Pointers Sorting 👍 18724 👎 661


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        p1, p2 = 0, l - 1

        for idx in range(l):

            if idx > p2:
                break

            while nums[idx] == 2 and idx <= p2 :
                nums[idx], nums[p2] = nums[p2], nums[idx]
                p2 -= 1

            if nums[idx] == 0:
                nums[idx], nums[p1] = nums[p1], nums[idx]
                p1 += 1

# leetcode submit region end(Prohibit modification and deletion)
