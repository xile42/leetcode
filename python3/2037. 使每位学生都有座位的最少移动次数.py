class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        return sum(abs(i - j) for i, j in zip(sorted(seats, reverse=True), sorted(students, reverse=True)))
