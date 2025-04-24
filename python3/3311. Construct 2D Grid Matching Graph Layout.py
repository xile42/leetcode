from math import sqrt
from typing import List
from collections import defaultdict, Counter


class Solution:

    def update1(self, node):

        self.results[0] = node
        idx = 1
        visit = [False for _ in range(self.n)]
        visit[node] = True
        while idx < self.n:
            for current_node in self.graph[self.results[idx-1]]:
                if visit[current_node] is False:
                    visit[current_node] = True
                    self.results[idx] = current_node
                    idx += 1
                    break

    def bfs(self, node):

        for next_node in self.graph[node]:
            if self.degrees[next_node] == 2:
                self.path = [node, next_node]
                return

        path = [node]
        current_node = node
        while True:
            for next_node in self.graph[current_node]:
                if next_node in path:
                    continue
                if self.degrees[next_node] == 3:
                    path.append(next_node)
                    current_node = next_node
                    break
                elif self.degrees[next_node] == 2:
                    self.path = path + [next_node]
                    return

    def update(self):
        # print(self.results)
        for jdx in range(1, self.n):
            for idx in range(0, self.m):
                left = self.results[idx][jdx-1]
                for candidate_node in self.graph[left]:
                    if self.visit[candidate_node] is False:
                        self.results[idx][jdx] = candidate_node
                        self.visit[candidate_node] = True
                        break
                    # print(idx, jdx, left, self.graph[left], self.results[idx][jdx])

    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        self.n = n
        self.graph = defaultdict(set)
        self.degrees = defaultdict(int)
        for i, j in edges:
            self.graph[i].add(j)
            self.graph[j].add(i)
            self.degrees[i] += 1
            self.degrees[j] += 1

        if min(self.degrees.values()) == 1:
            self.results = [-1 for _ in range(n)]
            for i in self.degrees:
                if self.degrees[i] == 1:
                    self.update1(i)
                    break
            self.results = [self.results]
        else:
            self.path = None
            for i in self.degrees:
                if self.degrees[i] == 2:
                    self.bfs(i)
                    break
            # print(self.path)
            self.m = len(self.path)
            self.n = n // self.m
            self.results = [[-1 for _ in range(self.n)] for _ in range(self.m)]
            for idx in range(self.m):
                self.results[idx][0] = self.path[idx]
            self.visit = [False for _ in range(n)]
            for i in self.path:
                self.visit[i] = True
            self.update()

        return self.results
