class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        raw_ans = list()

        def check(i, j, cur):

            for x, y in cur:
                if j == y or abs(x - i) == abs(y - j):
                    return False

            return True

        def dfs(cur):

            nonlocal raw_ans
            if len(cur) == n:
                raw_ans.append(cur)
                return

            i = len(cur)
            for j in range(n):
                if check(i, j, cur):
                    dfs(cur + [[i, j]])

        dfs([])

        ans = list()
        for path in raw_ans:
            t = [["." for _ in range(n)] for _ in range(n)]
            for i, j in path:
                t[i][j] = "Q"
            ans.append(["".join(row) for row in t])

        return ans
            
