class Solution:

    def makeStringsEqual(self, s: str, target: str) -> bool:
        a = target.count("1")
        b = s.count("1")
        if (a > 0 and b == 0) or (a == 0 and b > 0):
            return False

        return True
