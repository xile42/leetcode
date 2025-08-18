class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        d = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        cr = Counter()
        cc = Counter()

        for i, x in enumerate(arr):
            r, c = d[x]
            cr[r] += 1
            cc[c] += 1
            if cr[r] == n or cc[c] == m:
                return i
