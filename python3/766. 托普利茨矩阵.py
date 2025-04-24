class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m, n = len(matrix), len(matrix[0])
        d = dict()
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                if i - j in d and d[i - j] != v:
                    return False
                d[i - j] = v

        return True
