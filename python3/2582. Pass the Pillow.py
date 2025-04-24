class Solution:

    def passThePillow(self, n: int, time: int) -> int:

        round = time // (n - 1)
        remain = time % (n - 1)
        if round & 1:
            return list(range(1, n+1))[::-1][remain]
        else:
            return list(range(1, n+1))[remain]
