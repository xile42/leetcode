class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        n = len(adjacentPairs) + 1
        g = defaultdict(list)
        degrees = defaultdict(int)
        for u, v in adjacentPairs:
            g[u].append(v)
            g[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        start = next(node for node, degree in degrees.items() if degree == 1)
        ans = list()
        ans.append(start)
        while len(ans) < n:
            node = ans[-1]
            for neighbor in g[node]:
                if neighbor != ans[-2] if len(ans) > 1 else True:
                    ans.append(neighbor)
                    break

        return ans
