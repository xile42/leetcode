### 题目不一定入库，这里备份

# 2025 年浦东新区人工智能创新应用竞赛 Q2 认识天平
# 链接：https://leetcode.cn/contest/2025_pudong_ai/problems/R7aJ7z/


# 物理老师设计了一个需要大家借助天平完成的实验。
# 老师将n个砝码摆成一排，每个砝码的质量按摆放顺序存于数组weight中。
# 现在老师请同学取走其中某一个砝码，使得 取走砝码后奇数位的砝码质量之和与当前偶数位的砝码质量之和相等。若可以实现，请返回有多少种解答方法；否则请返回-1。


# 1 <= weight.length <= 10^5
# 0 <= weight[i] <= 1000


class Solution:

    def numWays(self, weight: List[int]) -> int:

        n = len(weight)
        if n == 1:
            return 1

        pre = [0] * n
        pre[0] = weight[0]
        pre[1] = weight[1]
        for i in range(2, n):
            pre[i] = pre[i - 2] + weight[i]

        suf = [0] * n
        suf[n - 1] = weight[n - 1]
        suf[n - 2] = weight[n - 2]
        for i in range(n - 3, -1, -1):
            suf[i] = suf[i + 2] + weight[i]

        ans = 0
        for i in range(n):
            left_1 = pre[i - 1] if i - 1 >= 0 else 0
            left_2 = pre[i - 2] if i - 2 >= 0 else 0
            right_1 = suf[i + 1] if i + 1 < n else 0
            right_2 = suf[i + 2] if i + 2 < n else 0
            if left_1 + right_2 == left_2 + right_1:
                ans += 1

        return -1 if ans == 0 else ans
