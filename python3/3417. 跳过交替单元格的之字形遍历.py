class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        g = list()
        for row in range(len(grid)):
            if row & 1:
                g.extend(grid[row][::-1])
            else:
                g.extend(grid[row])

        ans = g[::2]

        return ans