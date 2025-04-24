class Solution:

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        m, n = len(matrix), len(matrix[0])
        ans = matrix.copy()
        mx = [max(row) for row in list(zip(*matrix))]
        for i in range(m):
            for j in range(n):
                if ans[i][j] == -1:
                    ans[i][j] = mx[j]

        return ans
