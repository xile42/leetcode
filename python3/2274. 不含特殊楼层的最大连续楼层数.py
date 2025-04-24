class Solution:

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        ns = [bottom] + sorted(special) + [top]
        intervals = [ns[i] - ns[i - 1] - 1 for i in range(1, len(ns))]
        intervals[0] += 1
        intervals[-1] += 1

        return max(intervals)
