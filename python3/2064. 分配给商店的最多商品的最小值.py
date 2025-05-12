class Solution:

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def check(x):

            return sum(ceil(n / x) for n in quantities) <= n

        left = 1
        right = max(quantities)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
