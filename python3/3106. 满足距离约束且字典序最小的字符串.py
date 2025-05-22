class Solution:

    def getSmallestString(self, s: str, k: int) -> str:

        ans = list(s)
        cur = 0
        for i, c in enumerate(ans):
            dis = min(ord(c) - ord("a"), 26 - (ord(c) - ord("a")))
            if cur + dis <= k:
                cur += dis
                ans[i] = "a"
            else:
                ans[i] = chr(ord(c) - (k - cur))
                cur = k
                break

        return "".join(ans)
