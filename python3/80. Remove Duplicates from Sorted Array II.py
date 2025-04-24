# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice. The relative
# order of the elements should be kept the same.
#
#  Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the
# first k elements of nums should hold the final result. It does not matter what
# you leave beyond the first k elements.
#
#  Return k after placing the final result in the first k slots of nums.
#
#  Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
#  Custom Judge:
#
#  The judge will test your solution with the following code:
#
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#
#
#  If all assertions pass, then your solution will be accepted.
#
#
#  Example 1:
#
#
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#  Example 2:
#
#
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements
# of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 3 * 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums is sorted in non-decreasing order.
#
#
#  Related Topics Array Two Pointers 👍 7038 👎 1361


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        slow = 2  # first two is always valid
        for fast in range(slow, len(nums)):
            if nums[fast] == nums[slow-2]:
                continue
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow

# leetcode submit region end(Prohibit modification and deletion)
