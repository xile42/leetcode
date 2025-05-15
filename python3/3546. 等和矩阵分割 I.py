class Solution:

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        acc_rows = list(accumulate(rows))
        acc_cols = list(accumulate(cols))
        _all = acc_rows[-1]

        if _all & 1:
            return False

        return _all // 2 in acc_rows or _all // 2 in acc_cols
