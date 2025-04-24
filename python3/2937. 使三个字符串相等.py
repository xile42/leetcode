class Solution:

    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        if s1 == s2 == s3:
            return 0

        ans = 0
        for c1, c2, c3 in zip(s1, s2, s3):
            if c1 == c2 == c3:
                ans += 1
            else:
                break

        return -1 if ans == 0 else len(s1) - ans + len(s2) - ans + len(s3) - ans
