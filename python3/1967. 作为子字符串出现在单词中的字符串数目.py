class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        return sum(1 if p in word else 0 for p in patterns)
