### 题目不一定入库，这里备份

# 2025 年浦东新区人工智能创新应用竞赛 Q3 灯光调整
# 链接：https://leetcode.cn/contest/2025_pudong_ai/problems/MWmcf7/


# 灯光师需要调整灯光的亮度。brightness[i] 表示第 i 盏照明灯的初始亮度。
# 灯光师有一个控制器，每次操作可以选择任意 一段连续的照明灯，将其中所有灯的亮度 调高 1 或 降低 1。
# 请返回灯光师使所有灯的亮度一致所需要的 最小操作次数。


# 2 <= brightness.length <= 10^5
# 0 <= brightness[i] <= 10^4


class Solution:

    def lightAdjustment(self, brightness: List[int]) -> int:

        n = len(brightness)
        ns = [brightness[i] - brightness[0] for i in range(n)]
        diff = [0] + [ns[i] - ns[i - 1] for i in range(1, n)]

        a = b = 0
        for v in diff:
            if v > 0:
                a += v
            else:
                b += -v

        return max(a, b)
