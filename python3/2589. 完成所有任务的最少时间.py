class Solution:

    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda x: x[1])
        ans = 0
        run = [False] * (tasks[-1][1] + 1)
        for s, e, need in tasks:
            covered = sum(run[s:e + 1])
            need = max(need - covered, 0)
            ans += need
            if need:
                for i in range(e, s - 1, -1):
                    if not run[i]:
                        run[i] = True
                        need -= 1
                    if not need:
                        break

        return ans
