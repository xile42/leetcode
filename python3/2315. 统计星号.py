class Solution:

    def countAsterisks(self, s: str) -> int:

        return sum(Counter(sub)["*"] for sub in s.split("|")[::2])
