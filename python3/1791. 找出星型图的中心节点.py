class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:

        for k, v in Counter(edges[0] + edges[1]).items():
            if v == 2:
                return k
