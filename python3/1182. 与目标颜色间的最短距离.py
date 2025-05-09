class Solution:

    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        d = defaultdict(list)
        for i, c in enumerate(colors):
            d[c].append(i)

        ans = list()
        for i, c in queries:
            if not d[c]:
                ans.append(-1)
                continue
            j = bisect_left(d[c], i)
            diff = inf
            if j < len(d[c]):
                diff = min(diff, abs(i - d[c][j]))
            if j:
                diff = min(diff, abs(i - d[c][j - 1]))
            ans.append(diff)

        return ans
