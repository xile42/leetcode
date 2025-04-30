MX = 11
f = [[] for _ in range(MX)]
f[1] = [TreeNode()]
for i in range(2, MX):  # 计算 f[i]
    f[i] = [TreeNode(0, left, right)
            for j in range(1, i)  # 枚举左子树叶子数
            for left in f[j]  #  枚举左子树
            for right in f[i - j]]  # 枚举右子树

class Solution:

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        return f[(n + 1) // 2] if n % 2 else []
