class Solution:

    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)

        pre = [0] * n
        pre[0] = 1 if customers[0] == "N" else 0
        for i in range(1, n):
            pre[i] = pre[i - 1] + (1 if customers[i] == "N" else 0)

        suf = [0] * n
        suf[-1] = 1 if customers[-1] == "Y" else 0
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + (1 if customers[i] == "Y" else 0)

        ans = None
        cur = inf
        for i in range(n + 1):
            left = 0 if i == 0 else pre[i - 1]
            right = 0 if i == n else suf[i]
            if left + right < cur:
                cur = left + right
                ans = i

        return ans
