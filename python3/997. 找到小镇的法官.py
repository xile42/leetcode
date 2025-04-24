class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        ind, outd = Counter(), Counter()
        for a, b in trust:
            ind[b] += 1
            outd[a] += 1

        ans = list()
        for k in range(1, n + 1):
            if ind[k] == n - 1 and outd[k] == 0:
                ans.append(k)

        return ans[0] if len(ans) == 1 else -1
