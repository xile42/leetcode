class Solution:

    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        ans = [-1] * n

        pre = [1] * n
        for i in range(n):
            if i == 0:
                continue
            else:
                if ratings[i] <= ratings[i - 1]:
                    pre[i] = 1
                else:
                    pre[i] = pre[i - 1] + 1

        suf = [1] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            else:
                if ratings[i] <= ratings[i + 1]:
                    suf[i] = 1
                else:
                    suf[i] = suf[i + 1] + 1

        for i in range(n):
            ans[i] = max(pre[i], suf[i])

        return sum(ans)
