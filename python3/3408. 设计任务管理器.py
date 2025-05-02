from heapq import heappop


class TaskManager:

    def __init__(self, tasks: List[List[int]]):

        self.h = list()
        self.map = dict()
        self.valid = dict()

        for u, t, p in tasks:
            self.h.append([-p, -t])
            self.map[t] = u
            self.valid[t] = p

        heapify(self.h)

    def add(self, userId: int, taskId: int, priority: int) -> None:

        heappush(self.h, [-priority, -taskId])
        self.map[taskId] = userId
        self.valid[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:

        heappush(self.h, [-newPriority, -taskId])
        self.valid[taskId] = newPriority

    def rmv(self, taskId: int) -> None:

        if taskId in self.valid:
            del self.valid[taskId]

    def execTop(self) -> int:

        while self.h:
            p, t = heappop(self.h)
            p = -p
            t = -t
            if t not in self.valid or self.valid[t] != p:
                continue
            self.rmv(t)
            return self.map[t]

        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()©leetcode