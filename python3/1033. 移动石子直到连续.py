class Solution:

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        a, b, c = sorted([a, b, c])
        mn = 2
        if b - a == 2 or c - b == 2:
            mn = 1
        else:
            if a == b - 1:
                mn -= 1
            if b == c - 1:
                mn -= 1
        mx = b - a - 1 + c - b - 1

        return [mn, mx]
