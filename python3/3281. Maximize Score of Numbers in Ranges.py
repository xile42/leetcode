class Solution:

    def check(self, step, intervals, left, right):

        left_max = left
        for interval in intervals:

            start, end = interval
            right_min = left_max + step

            if right_min > end:
                self.success = False
                return

            left_max = max(right_min, start)

    def maxPossibleScore(self, start, d: int) -> int:

        intervals = list()
        for this_start in start:
            intervals.append([this_start, this_start+d])

        intervals = sorted(intervals)

        this_interval = intervals.pop(0)
        left = this_interval[0]
        this_interval = intervals[-1]  # no pop
        right = this_interval[-1]

        search_left, search_right = 0, right - left
        valid_results = list()
        while search_left <= search_right:

            mid = search_left + (search_right - search_left) // 2
            self.success = True
            self.check(mid, intervals, left, right)
            if self.success:
                valid_results.append(mid)
                search_left = mid + 1
            else:
                search_right = mid - 1

        return max(valid_results)


if __name__ == '__main__':

    foo = Solution()
    print(foo.maxPossibleScore([0,9,2,9], 2))

