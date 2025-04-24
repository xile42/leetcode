import math
from typing import List


class Solution:

    # @cache
    # def solve(self, target, base):
    #
    #     left = 0
    #     right = pow(10, 5)
    #
    #     if target < base:
    #         return 0
    #
    #     while left <= right:
    #         mid = left + (right-left) // 2
    #         value = base * ((mid+1)*mid) // 2
    #         if value == target:
    #             return mid
    #         elif value < target:
    #             value_next = base * ((mid+1+1)*(mid+1)) // 2
    #             if value_next == target:
    #                 return mid + 1
    #             elif value_next > target:
    #                 return mid
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    #     return left

    def solve(self, target, base):

        return math.floor((-1+math.sqrt(1+8*target//base))//2)

    def check(self, m, workers, seconds):

        finished = 0
        for v in workers:
            m_reduced = self.solve(seconds, v)
            finished += m_reduced

        return finished >= m

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        left = 1
        right = pow(10, 17)
        workerTimes = sorted(workerTimes, reverse=True)

        valid_results = list()
        while left <= right:
            mid = left + (right-left) // 2
            if self.check(mountainHeight, workerTimes, mid):
                if not self.check(mountainHeight, workerTimes, mid-1):
                    return mid
                valid_results.append(mid)
                right = mid - 1
            else:
                if self.check(mountainHeight, workerTimes, mid+1):
                    return mid + 1
                left = mid + 1

        return min(valid_results)


if __name__ == '__main__':

    foo = Solution()
    result = foo.minNumberOfSeconds(99, [1, 57])
    print(result)
