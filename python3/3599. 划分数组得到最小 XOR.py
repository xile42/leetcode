class Solution:

    def minXor(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ nums[i]

        def get(i, j):

            if i == 0:
                return pre[j]

            return pre[j] ^ pre[i - 1]

        dp = [[inf] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = get(0, i - 1)

        for j in range(2, k + 1):
            for i in range(j, n + 1):
                min_val = inf
                for t in range(i - 1, j - 2, -1):
                    cur = max(dp[t][j - 1], get(t, i - 1))
                    if cur < min_val:
                        min_val = cur
                        if min_val == 0:
                            break
                dp[i][j] = min_val

        return dp[n][k]
