class Solution:

    def trap(self, height: List[int]) -> int:

        pre = [height[0]]
        for i in height[1:]:
            pre.append(max(pre[-1], i))

        suf = [height[-1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            suf[i] = max(suf[i + 1], height[i])

        ans = 0
        for i in range(len(height)):
            ans += min(pre[i], suf[i]) - height[i]

        return ans
