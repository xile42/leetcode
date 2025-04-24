class Solution:

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        xys = reduce(add, [[(x, y) for y in range(cols)] for x in range(rows)])
        ans = list()
        for x, y in xys:
            ans.append([[x, y], abs(x - rCenter) + abs(y - cCenter)])

        return [x[0] for x in sorted(ans, key=lambda x: x[1])]
