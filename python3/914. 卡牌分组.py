class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        c = Counter(deck)

        return gcd(*c.values()) >= 2
