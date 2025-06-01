class Solution:

    def minOperations(self, k: int) -> int:

        if k == 1:
            return 0

        ans = inf
        cur = 1
        cnt = 0
        while cur < k:
            ans = min(ans, cnt + ceil(k / cur) - 1)
            cur += 1
            cnt += 1

        return ans
