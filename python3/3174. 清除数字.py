class Solution:

    def clearDigits(self, s: str) -> str:

        ans = str()
        cnt = 0
        for c in s[::-1]:
            if c.isdigit():
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    ans += c

        return ans[::-1]
