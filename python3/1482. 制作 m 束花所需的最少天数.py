class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def check(d):

            ns = [1 if t <= d else 0 for t in bloomDay]
            ans = 0
            for c, ite in groupby(ns):
                if c == 1:
                    ans += len(list(ite)) // k

            return ans >= m

        left = 1
        right = max(bloomDay)

        if m * k > len(bloomDay):
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
