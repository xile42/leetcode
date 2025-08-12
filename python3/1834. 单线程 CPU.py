class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        tasks = [[s, t, i] for i, (s, t) in enumerate(tasks)]
        tasks.sort()
        h = list()
        ans = list()
        i = cur = 0

        while h or i < n:

            if not h and cur < tasks[i][0]:
                cur = tasks[i][0]

            while i < n and tasks[i][0] <= cur:
                s, t, idx = tasks[i]
                heappush(h, [t, idx])
                i += 1

            t, idx = heappop(h)
            ans.append(idx)
            cur += t

        return ans
