class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        c = Counter()
        for row in matrix:
            c[min(row)] += 1
        for row in list(zip(*matrix)):
            c[max(row)] += 1

        return [k for k, v in c.items() if v == 2]
