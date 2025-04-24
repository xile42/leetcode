class Solution:

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        return (ord(coordinate1[0]) - ord("a") + int(coordinate1[1])) & 1 == (ord(coordinate2[0]) - ord("a") + int(coordinate2[1])) & 1
