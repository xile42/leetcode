class Solution:

    def isBoomerang(self, points: List[List[int]]) -> bool:

        i, j, k = points
        if i == j or j == k or k == i:
            return False

        k1 = inf if i[0] - j[0] == 0 else (i[1] - j[1]) / (i[0] - j[0])
        k2 = inf if k[0] - j[0] == 0 else (k[1] - j[1]) / (k[0] - j[0])

        return k1 != k2
