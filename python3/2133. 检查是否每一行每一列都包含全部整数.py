class Solution:

    def checkValid(self, matrix: List[List[int]]) -> bool:

        c = Counter()
        for i, row in enumerate(matrix):
            for n in row:
                if c[n] != i:
                    return False
                c[n] += 1

        for i, row in enumerate(list(zip(*matrix))):
            for n in row:
                if c[n] != len(matrix) + i:
                    return False
                c[n] += 1

        return True
