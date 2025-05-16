class Solution:

    def statisticalResult(self, arrayA: List[int]) -> List[int]:

        if not arrayA:
            return list()

        n = len(arrayA)
        pre = [1] * n
        suf = [1] * n
        pre[0] = arrayA[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] * arrayA[i]
        suf[-1] = arrayA[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * arrayA[i]

        ans = list()
        for i in range(n):
            ans.append((1 if i == 0 else pre[i - 1]) * (1 if i == n - 1 else suf[i + 1]))

        return ans
