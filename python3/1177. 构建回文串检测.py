class Solution:

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        ans = list()
        acc = [[0] * 26]
        for c in s:
            acc.append(copy.deepcopy(acc[-1]))
            acc[-1][ord(c) - ord("a")] += 1

        for l, r, k in queries:
            cnt = 0
            for i in range(26):
                cnt += (acc[r + 1][i] - acc[l][i]) & 1
            ans.append(True if floor(cnt / 2) <= k else False)

        return ans
