from typing import List


class Solution:

    def check(self, value):

        results = 0
        for time_need in self.time:
            results += value // time_need

        return True if results >= self.total_trips else False

    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        self.time = time
        self.total_trips = totalTrips
        left, right = 1, pow(10, 14)
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':

    foo = Solution()
    print(foo.minimumTime([9, 5, 2, 7, 6, 6, 6], 95279527))
