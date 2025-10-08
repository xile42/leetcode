class Solution:

    def minimumPartition(self, s: str, k: int) -> int:

        ans = 1
        cur = 0
        for c in s:
            v = int(c)
            vv = cur * 10 + v
            if vv > k:
                ans += 1
                if cur == 0 or v > k:
                    return -1
                cur = v
            else:
                cur = vv

        return ans
