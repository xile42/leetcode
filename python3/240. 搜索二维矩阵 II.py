class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if row[0] <= target <= row[-1] and target in row:
                return True

        return False
