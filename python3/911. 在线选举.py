class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.ans = list()
        c = Counter()
        mx = None
        for t, p in zip(times, persons):
            c[p] += 1
            if mx is None or c[p] >= c[mx]:
                mx = p
            self.ans.append(mx)
        self.times = times

    def q(self, t: int) -> int:

        i = bisect_right(self.times, t)

        return self.ans[i - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)