class Solution:

    def circularGameLosers(self, n: int, k: int) -> List[int]:

        players = set(range(n))
        survive = set()
        survive.add(0)
        round = 1
        while True:
            guy = ((round * (round + 1)) / 2 * k) % n
            if guy in survive:
                break
            survive.add(guy)
            round += 1

        dead = players - survive
        dead = sorted([i + 1 for i in dead])

        return dead
