class Solution:

    def minSteps(self, s: str, t: str) -> int:

        cs, ct = Counter(s), Counter(t)

        return sum((cs - ct).values()) + sum((ct - cs).values())
