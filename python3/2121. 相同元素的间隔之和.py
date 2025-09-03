class Solution:

    def getDistances(self, arr: List[int]) -> List[int]:

        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
        ans = [0] * len(arr)
        for p in pos.values():
            ans[p[0]] = s = sum(i - p[0] for i in p)
            n = len(p)
            for i in range(1, n):
                s += (2 * i - n) * (p[i] - p[i - 1])
                ans[p[i]] = s

        return ans
