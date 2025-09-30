class Solution:

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        c = Counter()
        groups = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            groups[u].append(w)

        for u, group in groups.items():
            if len(group) < 3:
                continue
            n = len(group)
            vis = set()
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if (group[i], group[j], group[k]) not in vis:
                            vis.add((group[i], group[j], group[k]))
                            c[(group[i], group[j], group[k])] += 1

        ans = None
        cur = -inf
        for k, v in c.items():
            if v > cur or (v == cur and (ans is None or k < ans)):
                ans = k
                cur = v

        return ans
