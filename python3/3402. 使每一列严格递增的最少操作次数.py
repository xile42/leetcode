class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        grid = list(zip(*grid))
        ans = 0
        for row in grid:
            cur = row[0]
            for n in row[1:]:
                ans += max(cur + 1 - n, 0)
                cur = max(cur + 1, n)

        return ans