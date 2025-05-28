class Leaderboard:

    def __init__(self):

        self.c = Counter()

    def addScore(self, playerId: int, score: int) -> None:

        self.c[playerId] += score

    def top(self, K: int) -> int:

        kvs = list(self.c.items())
        kvs.sort(key=lambda x: x[1], reverse=True)

        return sum([kv[1] for kv in kvs[:K]])

    def reset(self, playerId: int) -> None:

        del self.c[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)