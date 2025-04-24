class Solution:

    def isFlipedString(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False

        if s1 == s2:
            return True

        for i in range(len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True

        return False
