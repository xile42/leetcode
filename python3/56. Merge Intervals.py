# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals that
# cover all the intervals in the input.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#
#  Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
#  Constraints:
#
#
#  1 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁴
#
#
#  Related Topics Array Sorting 👍 22353 👎 789


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    def merge_two(self, interval_i, interval_j):
        start, end = interval_i
        other_start, other_end = interval_j
        if end >= other_start:
            return True, [start, max(end, other_end)]
        else:
            return False, []

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        results = list()

        while len(intervals) > 1:
            merge_flag, merge_results = self.merge_two(intervals[0], intervals[1])
            if merge_flag:
                intervals.pop(0)
                intervals.pop(0)
                intervals.insert(0, merge_results)
            else:
                results.append(intervals[0])
                intervals.pop(0)

        results.append(intervals[0])

        return results

# leetcode submit region end(Prohibit modification and deletion)
