class Solution:

    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        h_server = list()
        for i, v in enumerate(servers):
            heappush(h_server, (v, i))
        h_unlock = list()

        ans = list()
        task_queue = deque()
        for cur, need in enumerate(tasks):
            while h_unlock and h_unlock[0][0] <= cur:
                v, i = heappop(h_unlock)
                heappush(h_server, (servers[i], i))
            task_queue.append((cur, need))
            while h_server and task_queue:
                v, i = heappop(h_server)
                task_id, task_need = task_queue.popleft()
                ans.append(i)
                heappush(h_unlock, (cur + task_need, i))

        while task_queue:
            if not h_server:
                cur = h_unlock[0][0]
                while h_unlock and h_unlock[0][0] <= cur:
                    v, i = heappop(h_unlock)
                    heappush(h_server, (servers[i], i))
            while h_server and task_queue:
                v, i = heappop(h_server)
                task_id, task_need = task_queue.popleft()
                ans.append(i)
                heappush(h_unlock, (cur + task_need, i))

        return ans
