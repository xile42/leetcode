class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:

        def check(x):

            return sum(floor(sqrt(x / r)) for r in ranks) >= cars

        left = 1
        right = min(ranks) * cars * cars
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
