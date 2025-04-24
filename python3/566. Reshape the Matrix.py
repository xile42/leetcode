class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        results = list()
        for idx in range(r):
            row = list()
            for jdx in range(c):
                index = idx * c + jdx
                x = index // n
                y = index % n
                row.append(mat[x][y])
            results.append(row)

        return results
