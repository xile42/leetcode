from itertools import groupby


class Solution:

    def largeGroupPositions(self, s: str) -> List[List[int]]:

        cur = 0
        result = list()
        for char, ite in groupby(s):
            l = len(list(ite))
            if l >= 3:
                result.append([cur, cur+l-1])
            cur += l

        return result
