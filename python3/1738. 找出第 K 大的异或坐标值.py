class Solution:

    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ x

        return sorted(x for row in s[1:] for x in row[1:])[-k]
