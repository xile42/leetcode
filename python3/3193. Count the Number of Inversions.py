class Solution:

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:

        MOD = 1_000_000_007
        req = [-1] * n
        req[0] = 0
        for end, cnt in requirements:
            req[end] = cnt
        if req[0]:
            return 0

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return 1
            r = req[i - 1]
            if r >= 0:
                return dfs(i - 1, r) if r <= j <= i + r else 0
            return sum(dfs(i - 1, j - k) for k in range(min(i, j) + 1)) % MOD
        return dfs(n - 1, req[-1])
