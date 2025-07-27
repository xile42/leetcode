class Solution:

    def shortestSuperstring(self, s1: str, s2: str) -> str:

        def f(s1, s2):

            for i in range(len(s1)):
                s = s1[:i] + s2
                if len(s) < len(s1):
                    s += s1[i:]
                if s[:len(s1)] == s1:
                    return s

            return s1 + s2

        if s1 in s2:
            return s2

        if s2 in s1:
            return s1

        ans1 = f(s1, s2)
        ans2 = f(s2, s1)

        return ans1 if len(ans1) < len(ans2) else ans2
