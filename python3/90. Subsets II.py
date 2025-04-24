# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
#  The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
#  Example 1:
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#  Example 2:
#  Input: nums = [0]
# Output: [[],[0]]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#
#
#  Related Topics Array Backtracking Bit Manipulation 👍 9855 👎 328


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        from itertools import combinations

        results = list()
        for length in range(len(nums)+1):
            results += combinations(nums, length)

        results = [tuple(sorted(i)) for i in results]
        results = [list(i) for i in set(results)]

        return results

# leetcode submit region end(Prohibit modification and deletion)
