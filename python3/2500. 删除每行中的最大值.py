class Solution:

    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        grid = [sorted(row) for row in grid]

        return sum(max(col) for col in list(zip(*grid)))
