class Solution:

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        rows = [0] * m
        cols = [0] * n
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        odd_row = sum([1 if i & 1 else 0 for i in rows])
        odd_col = sum([1 if i & 1 else 0 for i in cols])

        return odd_row * (n - odd_col) + odd_col * (m - odd_row)
