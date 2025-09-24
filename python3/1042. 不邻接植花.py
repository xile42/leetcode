class Solution:

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        ans = [-1] * n
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        def f(i, c):

            for j in g[i]:
                if ans[j] == c:
                    return False
            ans[i] = c
            for j in g[i]:
                if ans[j] == -1:
                    for c2 in range(1, 5):
                        if f(j, c2):
                            break
                    if ans[j] == -1:
                        ans[i] = -1
                        return False

            return True

        for i in range(n):
            if ans[i] != -1:
                continue
            for c in range(1, 5):
                if f(i, c):
                    break
            else:  # 题目保证答案存在
                return list()

        return ans
