class Solution:

    def edgeScore(self, edges: List[int]) -> int:

        c = Counter()
        for i, j in enumerate(edges):
            c[j] += i

        kvs = sorted([[-v, k] for k, v in c.items()])

        return kvs[0][1]
