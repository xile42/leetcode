class Solution:

    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        n = len(colsum)
        ans = [[0 for _ in range(n)] for _ in range(2)]

        both = 0
        optional = 0
        for v in colsum:
            if v == 2:
                both += 1
            elif v == 1:
                optional += 1

        tar0 = upper - both
        tar1 = lower - both
        if tar0 < 0 or tar1 < 0 or tar0 + tar1 != optional:
            return list()

        for i, v in enumerate(colsum):
            if v == 2:
                ans[0][i] = 1
                ans[1][i] = 1
            elif v == 1:
                if tar0 > 0:
                    ans[0][i] = 1
                    tar0 -= 1
                else:
                    ans[1][i] = 1

        return ans
