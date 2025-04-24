class Solution:

    def checkOnesSegment(self, s: str) -> bool:

        return Counter([i for i, _ in groupby(s)])["1"] <= 1
