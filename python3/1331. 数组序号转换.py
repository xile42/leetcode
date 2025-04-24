class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        d = dict()
        sa = sorted(arr)
        t = 1
        for i, v in enumerate(sa):
            if v not in d:
                d[v] = t
                t += 1

        return [d[v] for v in arr]
