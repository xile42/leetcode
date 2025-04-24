class Solution:

    def balancedStringSplit(self, s: str) -> int:

        cur = [0, 0]
        cnt = 0
        for c in s:
            if c == "L":
                cur[0] += 1
            else:
                cur[1] += 1
            if cur[0] == cur[1] and cur[0] > 0:
                cur = [0, 0]
                cnt += 1

        return cnt
