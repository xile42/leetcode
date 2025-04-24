class Solution:

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        c = Counter()
        for u, v in edges:
            c[v] += 1

        return [k for k in range(n) if c[k] == 0]
