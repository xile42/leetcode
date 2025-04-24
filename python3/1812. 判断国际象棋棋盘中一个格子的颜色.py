class Solution:

    def squareIsWhite(self, coordinates: str) -> bool:

        n = ord(coordinates[0]) - ord("a") + int(coordinates[1])

        return n & 1 != 1
