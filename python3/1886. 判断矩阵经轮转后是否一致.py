class Solution:

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def f(grid):
            return list(map(list, zip(*grid[::-1])))

        for _ in range(4):
            mat = f(mat)
            if mat == target:
                return True

        return False
