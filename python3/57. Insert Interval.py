# You are given an array of non-overlapping intervals intervals where intervals[
# i] = [starti, endi] represent the start and the end of the iᵗʰ interval and
# intervals is sorted in ascending order by starti. You are also given an interval
# newInterval = [start, end] that represents the start and end of another interval.
#
#  Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
#  Return intervals after the insertion.
#
#  Note that you don't need to modify intervals in-place. You can make a new
# array and return it.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
#  Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
#
#  Constraints:
#
#
#  0 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁵
#  intervals is sorted by starti in ascending order.
#  newInterval.length == 2
#  0 <= start <= end <= 10⁵
#
#
#  Related Topics Array 👍 10476 👎 823


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def merge(self, interval, other_interval):
        start, end = interval
        other_start, other_end = other_interval
        if other_start <= end:
            return True, [start, max(end, other_end)]
        return False, []

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        results = list()

        insert_idx = None
        for idx in range(len(intervals)):
            if intervals[idx][0] > newInterval[0]:
                insert_idx = idx
                break

        if insert_idx is None:
            insert_idx = len(intervals)
        intervals.insert(insert_idx, newInterval)
        if insert_idx > 1:
            results += intervals[:insert_idx-1]
            intervals = intervals[insert_idx-1:]

        none_merge_cnt = 0
        while len(intervals) > 1:
            merge_result, merge_interval = self.merge(intervals[0], intervals[1])
            if merge_result:
                intervals.pop(0)
                intervals.pop(0)
                intervals.insert(0, merge_interval)
            else:
                if none_merge_cnt >= 2:
                    break
                else:
                    none_merge_cnt += 1
                    this_interval = intervals.pop(0)
                    results.append(this_interval)

        results += intervals

        return results

# leetcode submit region end(Prohibit modification and deletion)
