"""
codeforces-python: 算法竞赛Python3模板库
#1: 矩阵基础操作
https://github.com/xile42/codeforces-python/blob/main/templates/math_matrix.py
"""
class MatrixBasics:

    @staticmethod
    def read_matrix(n: int) -> List[List[int]]:

        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)

        return matrix

    @staticmethod
    def copy_matrix(matrix: List[List[int]]) -> List[List[int]]:

        return [row[:] for row in matrix]

    @staticmethod
    def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:

        n, m = len(matrix), len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        for j in range(m):
            for i in range(n):
                ans[j][n - 1 - i] = matrix[i][j]

        return ans


class Solution:

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        matrix = MatrixBasics.rotate_matrix(boxGrid)
        m, n = len(matrix), len(matrix[0])

        cur_bottom = [m - 1 for _ in range(n)]

        for i in range(m - 1, -1, -1):
            for j in range(n):
                c = matrix[i][j]
                if c == ".":
                    continue
                elif c == "*":
                    cur_bottom[j] = i - 1
                else:
                    matrix[i][j] = "."
                    matrix[cur_bottom[j]][j] = "#"
                    cur_bottom[j] -= 1

        return matrix
