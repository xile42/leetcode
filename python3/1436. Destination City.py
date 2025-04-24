class Solution:

    def destCity(self, paths: List[List[str]]) -> str:

        in_d = defaultdict(int)
        out_d = defaultdict(int)
        for i, j in paths:
            in_d[j] += 1
            out_d[i] += 1

        for i in in_d:
            if out_d[i] == 0:
                return i
