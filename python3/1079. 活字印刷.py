class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        ans = list()
        n = len(tiles)
        cs = list(tiles)
        for i in range(1, n + 1):
            for sub_cs in combinations(cs, i):
                ans += permutations(sub_cs)

        return len(set(ans))
