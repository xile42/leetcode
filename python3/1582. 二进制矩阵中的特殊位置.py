class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        rows = [sum(row) for row in mat]
        cols = [sum(row) for row in list(zip(*mat))]

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    ans += 1

        return ans
