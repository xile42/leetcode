class Solution:

    def convertTime(self, current: str, correct: str) -> int:

        h1, h2 = int(current[:2]), int(correct[:2])
        m1, m2 = int(current[-2:]), int(correct[-2:])
        if current > correct:
            h2 += 24

        diff = (h2 * 60 + m2) - (h1 * 60 + m1)
        ans = 0
        for step in [60, 15, 5, 1]:
            while diff >= step:
                diff -= step
                ans += 1

        return ans
