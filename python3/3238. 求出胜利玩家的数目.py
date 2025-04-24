class Solution:
    
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        d = defaultdict(lambda : defaultdict(int))
        for p, c in pick:
            d[p][c] += 1

        ans = 0
        for p in d:
            if max(d[p].values()) > p:
                ans += 1

        return ans
