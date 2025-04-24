class Solution:

    def maxDistance(self, colors: List[int]) -> int:

        ans = -inf

        cur = 0
        tar = colors[-1]
        while colors[cur] == tar:
            cur += 1
        ans = max(ans, len(colors) - 1 - cur)

        cur = -1
        tar = colors[0]
        while colors[cur] == tar:
            cur -= 1
        ans = max(ans, len(colors) + cur)

        return ans
