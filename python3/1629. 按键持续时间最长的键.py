class Solution:

    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        releaseTimes = [0] + releaseTimes
        t = [releaseTimes[i] - releaseTimes[i - 1] for i in range(1, len(releaseTimes))]
        d = defaultdict(int)
        for i, c in enumerate(keysPressed):
            d[c] = max(d[c], t[i])
        max_v = max(d.values())
        for c in sorted(d.keys(), reverse=True):
            if d[c] == max_v:
                return c
