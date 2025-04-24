# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum
# to target.
#
#  Each number in candidates may only be used once in the combination.
#
#  Note: The solution set must not contain duplicate combinations.
#
#
#  Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
#  Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
#  Constraints:
#
#
#  1 <= candidates.length <= 100
#  1 <= candidates[i] <= 50
#  1 <= target <= 30
#
#
#  Related Topics Array Backtracking 👍 11013 👎 320


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    results = set()

    def search(self, nums, begin, used, target):

        for idx in range(begin, len(nums)):

            num = nums[idx]
            if idx > begin and nums[idx] == nums[idx-1]:
                continue
            if num == target:
                self.results.add(tuple(used+[num]))
                return
            elif num < target:
                self.search(nums, idx+1, used+[num], target-num)
            else:
                return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.results = set()
        sorted_candidates = sorted(candidates)
        self.search(sorted_candidates, 0, list(), target)
        return sorted(list(self.results))

# leetcode submit region end(Prohibit modification and deletion)
