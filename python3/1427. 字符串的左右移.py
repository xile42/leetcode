class Solution:

    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        for d, a in shift:
            a = a % len(s)
            if a and d:
                s = s[-a:] + s[:len(s)-a]
            elif a and not d:
                s = s[a:] + s[:a]

        return s
