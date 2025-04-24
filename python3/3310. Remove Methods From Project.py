from typing import List
from collections import defaultdict


class Solution:

    def fetch_children(self, node):

        results = set()
        results.add(node)
        visit = [False for _ in range(self.n)]
        queue = [node]

        while len(queue) > 0:
            current = queue.pop(0)
            visit[current] = True
            results |= self.children[current]
            for next_node in self.children[current]:
                if not visit[next_node]:
                    queue.append(next_node)

        return results

    def fetch_parents(self, suspicious):

        results = set()

        for node in suspicious:
            results |= self.parent[node]

        return results

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        self.n = n
        self.parent = defaultdict(set)
        self.children = defaultdict(set)

        for p, c in invocations:
            self.parent[c].add(p)
            self.children[p].add(c)

        suspicious = self.fetch_children(k)
        suspicious_parent = self.fetch_parents(suspicious)

        # print(suspicious_parent)
        # print(suspicious)

        if len(suspicious_parent - suspicious) == 0:
            return sorted(list(set(range(n)) - suspicious))

        return list(range(n))


if __name__ == '__main__':

    foo = Solution()
    print(foo.remainingMethods(5, 0, [[1,2],[0,2],[0,1],[3,4]]))
