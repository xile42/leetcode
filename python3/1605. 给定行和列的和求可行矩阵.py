class Solution:

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        m, n = len(rowSum), len(colSum)
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = min(rowSum[i], colSum[j])
                ans[i][j] = v
                rowSum[i] -= v
                colSum[j] -= v

        return ans
