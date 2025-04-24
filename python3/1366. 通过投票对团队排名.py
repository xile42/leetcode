class Solution:

    def rankTeams(self, votes: List[str]) -> str:

        m = len(votes[0])
        cnts = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                cnts[ch][i] -= 1  # 改成负数（相反数），方便比大小

        return ''.join(sorted(cnts, key=lambda ch: (cnts[ch], ch)))
