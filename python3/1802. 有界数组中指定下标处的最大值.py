class Solution:

    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def check(x):

            s = x
            left_cnt = index
            right_cnt = n - 1 - index

            if left_cnt <= x - 1:
                s += left_cnt * (2 * x - left_cnt - 1) // 2
            else:
                s += x * (x - 1) // 2
                s += left_cnt - (x - 1)

            if right_cnt <= x - 1:
                s += right_cnt * (2 * x - right_cnt - 1) // 2
            else:
                s += x * (x - 1) // 2
                s += right_cnt - (x - 1)

            return s <= maxSum

        left = 1
        right = maxSum
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
