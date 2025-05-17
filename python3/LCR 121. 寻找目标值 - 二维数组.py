class Solution:

    def findTargetIn2DPlants(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1] and target in row:
                return True

        return False
