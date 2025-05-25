class Solution:

    def maximumCandies(self, candies: List[int], k: int) -> int:

        def check(x):
            return sum(n // x for n in candies) >= k

        left = 1
        right = max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
