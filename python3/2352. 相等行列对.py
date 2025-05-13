class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:

        d = defaultdict(list)
        for i, row in enumerate(grid):
            d[tuple(row)].append(i)

        ans = 0
        for i, col in enumerate(list(zip(*grid))):
            ans += len(d[tuple(col)])

        return ans
