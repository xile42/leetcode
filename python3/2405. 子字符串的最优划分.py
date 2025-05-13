class Solution:

    def partitionString(self, s: str) -> int:

        ans = 1
        cnt = set()
        for c in s:
            if c in cnt:
                ans += 1
                cnt = {c}
            else:
                cnt.add(c)

        return ans
