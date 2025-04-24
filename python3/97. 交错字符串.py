class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def f(s1, s2, s3):

            if not s3:
                return True

            r1, r2 = False, False
            if s1 and s1[0] == s3[0]:
                r1 = f(s1[1:], s2, s3[1:])
            if s2 and s2[0] == s3[0]:
                r2 = f(s1, s2[1:], s3[1:])

            return r1 | r2

        return f(s1, s2, s3)
