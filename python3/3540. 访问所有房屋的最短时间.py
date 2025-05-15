class Solution:

    def minTotalTime(self, forward: List[int], backward: List[int], queries: List[int]) -> int:

        acc_for = list(accumulate(forward))
        acc_bac = list(accumulate(backward))
        if queries[0] != 0:
            queries = [0] + queries

        ans = 0
        for s, e in pairwise(queries):
            if s < e:
                ans1 = acc_for[e - 1] - (0 if s == 0 else acc_for[s - 1])
                ans2 = acc_bac[-1] - (acc_bac[e] - acc_bac[s])
            else:
                ans1 = acc_for[-1] - (acc_for[s - 1] - (0 if e == 0 else acc_for[e - 1]))
                ans2 = acc_bac[s] - acc_bac[e]
            ans += min(ans1, ans2)

        return ans
