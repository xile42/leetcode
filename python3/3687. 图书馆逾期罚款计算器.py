class Solution:

    def lateFee(self, daysLate: List[int]) -> int:

        return sum(map(lambda x: 1 if x == 1 else (2 * x if 2 <= x <= 5 else 3 * x), daysLate))
