class Solution:

    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:

        n = len(lane1)

        @cache
        def f(cur, left, idx):

            if cur >= n:
                return 0

            ans = list()
            gain = lane1[cur] if idx == 1 else lane2[cur]
            ans.append(gain + f(cur + 1, left, idx))
            if left:
                gain = lane2[cur] if idx == 1 else lane1[cur]
                ans.append(gain + f(cur + 1, left - 1, 1 - idx))
            ans.append(0)

            return max(ans)

        ans = -inf
        for start in range(n):
            ans = max(ans, lane1[start] + f(start + 1, 2, 1), lane2[start] + f(start + 1, 1, 0))

        return ans
