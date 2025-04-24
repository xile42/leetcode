class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(v):
            return sum(ceil(i / v) for i in piles) <= h

        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
