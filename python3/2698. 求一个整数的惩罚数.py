PRE_SUM = [0] * 1001
for i in range(1, 1001):
    s = str(i * i)
    n = len(s)
    def dfs(p: int, sum: int) -> bool:
        if p == n:  # 递归终点
            return sum == i  # i 符合要求
        x = 0
        for j in range(p, n):  # 枚举分割出从 s[p] 到 s[j] 的子串
            x = x * 10 + int(s[j])  # 子串对应的整数值
            if dfs(j + 1, sum + x):
                return True
        return False
    PRE_SUM[i] = PRE_SUM[i - 1] + (i * i if dfs(0, 0) else 0)


class Solution:

    def punishmentNumber(self, n: int) -> int:

        return PRE_SUM[n]
