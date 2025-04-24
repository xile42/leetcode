class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:

        m, n = len(strs), len(strs[0])
        cnt = 0
        for j in range(n):
            for i in range(1, m):
                if not strs[i][j] >= strs[i-1][j]:
                    cnt += 1
                    break

        return cnt
