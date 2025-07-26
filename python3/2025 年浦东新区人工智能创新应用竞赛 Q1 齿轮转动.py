### 题目不一定入库，这里备份

# 2025 年浦东新区人工智能创新应用竞赛 Q1 齿轮转动
# 链接：https://leetcode.cn/contest/2025_pudong_ai/problems/O7NW93/

# 某机械零部件上有一些不同规格的齿轮依次相连，ratio[i] 表示第 i 个齿轮的齿数。 某工程师为比较齿轮的实际转动值与理论值，将转动第 cnt 个齿轮 degree 度。 请返回所有齿轮的理论转动角度（反向转动为负角度）。
# 注意：齿轮转动时，任意相邻的两个齿轮转动齿数相同，且方向相反。

# 1 <= ratio.length <= 10^5
# 1 <= ratio[i] <= 10^6
# 0 <= cnt < ratio.length
# 1 <= degree <= 10^9
# 用例保证返回的每个齿轮的转动值均为整数，且其绝对值不超过 10^9


class Solution:

    def spinGears(self, ratio: List[int], cnt: int, degree: int) -> List[int]:

        n = len(ratio)
        ans = [0] * n
        ans[cnt] = degree

        for i in range(cnt + 1, n):
            ans[i] = (ans[i - 1] * ratio[i - 1]) // ratio[i] * (-1)

        for i in range(cnt - 1, -1, -1):
            ans[i] = (ans[i + 1] * ratio[i + 1]) // ratio[i] * (-1)

        return ans
