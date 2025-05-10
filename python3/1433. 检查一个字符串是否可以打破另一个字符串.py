class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        ns = list(zip(sorted(s1), sorted(s2)))

        return all(a >= b for a, b in ns) or all(a <= b for a, b in ns)
