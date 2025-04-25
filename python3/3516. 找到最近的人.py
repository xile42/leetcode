class Solution:

    def findClosest(self, x: int, y: int, z: int) -> int:

        a = abs(x - z)
        b = abs(y - z)

        return 1 if a < b else (2 if a > b else 0)
