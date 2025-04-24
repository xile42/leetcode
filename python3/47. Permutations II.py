# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
#  Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#
#  Related Topics Array Backtracking 👍 8554 👎 146


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    result = list()

    def search(self, nums, current):

        if len(nums) == 0:
            self.result.append(current)

        visited_this_layer = set()
        for idx, num in enumerate(nums):
            if num in visited_this_layer:
                continue
            visited_this_layer.add(num)
            self.search(nums[:idx] + nums[idx + 1:], current + [num])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())
        return self.result

# leetcode submit region end(Prohibit modification and deletion)
