class Solution:

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        
        col_sum = [sum(col) - 1 for col in zip(*grid)]  # 提前减一
        ans = 0
        for row in grid:
            row_sum = sum(row) - 1  # 提前减一
            ans += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)

        return ans
