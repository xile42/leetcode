class Solution:

    def dfs(self, i, j):
        if i == 0 or j == 0:
            return 0
        return self.dfs(i - 1, j) + self.dfs(i - 1, j - 1) + 1

    def superEggDrop(self, k: int, n: int) -> int:

        for i in count(1):
            if self.dfs(i, k) >= n:
                return i
