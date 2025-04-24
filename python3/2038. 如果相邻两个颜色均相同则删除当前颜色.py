class Solution:

    def winnerOfGame(self, colors: str) -> bool:

        a = b = 0
        for c, ite in groupby(colors):
            if c == "A":
                a += max(0, len(list(ite)) - 2)
            else:
                b += max(0, len(list(ite)) - 2)

        return a - 1 >= b
