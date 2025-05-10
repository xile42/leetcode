class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])

        i = 0
        for j in range(n):
            ii, jj = i, j
            ns = list()
            while 0 <= ii < m and 0 <= jj < n:
                ns.append(mat[ii][jj])
                ii += 1
                jj += 1
            ns.sort()
            ii, jj = i, j
            idx = 0
            while 0 <= ii < m and 0 <= jj < n:
                mat[ii][jj] = ns[idx]
                ii += 1
                jj += 1
                idx += 1

        j = 0
        for i in range(m):
            ii, jj = i, j
            ns = list()
            while 0 <= ii < m and 0 <= jj < n:
                ns.append(mat[ii][jj])
                ii += 1
                jj += 1
            ns.sort()
            ii, jj = i, j
            idx = 0
            while 0 <= ii < m and 0 <= jj < n:
                mat[ii][jj] = ns[idx]
                ii += 1
                jj += 1
                idx += 1

        return mat
