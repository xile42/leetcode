class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        row = [False for _ in range(m)]
        column = [False for _ in range(n)]

        for idx in range(m):
            for jdx in range(n):
                if matrix[idx][jdx] == 0:
                    row[idx] = True
                    column[jdx] = True

        for idx in range(m):
            if row[idx]:
                for jdx in range(n):
                    matrix[idx][jdx] = 0
        for jdx in range(n):
            if column[jdx]:
                for idx in range(m):
                    matrix[idx][jdx] = 0
