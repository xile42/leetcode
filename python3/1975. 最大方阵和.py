class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        ans = 0
        ns = list()
        n = len(matrix)
        cnt = 0

        for i in range(n):
            for j in range(n):
                v = matrix[i][j]
                if v < 0:
                    cnt += 1
                ns.append(abs(v))

        ns.sort()
        if cnt & 1:
            ns[0] *= -1

        return sum(ns)
