class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        ans = 0
        for i in range(n):
            if n & 1 and i == n // 2:
                continue
            ans += mat[i][i]
        for i in range(n):
            j = n - 1 - i
            ans += mat[i][j]

        return ans
