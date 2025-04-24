# You are given an undirected weighted graph of n nodes (0-indexed),
# represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the
# nodes a and b with a probability of success of traversing that edge succProb[i].
#
#  Given two nodes start and end, find the path with the maximum probability of
# success to go from start to end and return its success probability.
#
#  If there is no path from start to end, return 0. Your answer will be
# accepted if it differs from the correct answer by at most 1e-5.
#
#
#  Example 1:
#
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0
# , end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability
# of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
#
#
#  Example 2:
#
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0
# , end = 2
# Output: 0.30000
#
#
#  Example 3:
#
#
#
#
# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
#
#
#
#  Constraints:
#
#
#  2 <= n <= 10^4
#  0 <= start, end < n
#  start != end
#  0 <= a, b < n
#  a != b
#  0 <= succProb.length == edges.length <= 2*10^4
#  0 <= succProb[i] <= 1
#  There is at most one edge between every two nodes.
#
#
#  Related Topics Array Graph Heap (Priority Queue) Shortest Path 👍 3262 👎 79


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    result = 0

    # def search(self, graph, node, current_p, visit):  # dfs
    #
    #     if node == self.end:
    #         if current_p > self.result:
    #             self.result = current_p
    #         return
    #
    #     for other_node in range(len(graph)):
    #         if graph[node][other_node] != 0 and other_node not in visit:
    #             new_p = current_p * graph[node][other_node]
    #             if new_p <= self.result:
    #                 continue
    #             self.search(graph, other_node, new_p, visit+[other_node])

    # def search(self, graph, start):  # bfs
    #
    #     queue = list()
    #     queue.append([start, 1])
    #     nodes_p = [0 for _ in range(len(graph))]
    #     nodes_p[start] = 1
    #
    #     while len(queue) != 0:
    #         node, p = queue.pop(0)
    #
    #         if node == self.end:
    #             if p > self.result:
    #                 self.result = p
    #                 continue
    #
    #         for other_node in range(len(graph)):
    #             if graph[node][other_node] == 0:
    #                 continue
    #             new_p = p * graph[node][other_node]
    #             if new_p <= nodes_p[other_node]:
    #                 continue
    #             nodes_p[other_node] = new_p
    #             queue.append([other_node, new_p])

    def search(self, graph, start, n):  # bfs

        queue = list()
        queue.append([start, 1])
        nodes_p = [0 for _ in range(n)]
        nodes_p[start] = 1

        while len(queue) != 0:
            node, p = queue.pop(0)

            if node == self.end:
                if p > self.result:
                    self.result = p
                    continue

            for other_node, this_p in graph[node]:
                new_p = p * this_p
                if new_p <= nodes_p[other_node]:
                    continue
                nodes_p[other_node] = new_p
                queue.append([other_node, new_p])

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        # graph = [[0 for _ in range(n)] for _ in range(n)]
        # for idx in range(len(edges)):
        #     i, j = edges[idx]
        #     p = succProb[idx]
        #     graph[i][j] = p
        #     graph[j][i] = p

        from collections import defaultdict
        graph = defaultdict(list)
        for idx in range(len(edges)):
            i, j = edges[idx]
            p = succProb[idx]
            graph[i].append([j, p])
            graph[j].append([i, p])

        self.result = 0
        self.end = end_node
        # self.search(graph, start_node, 1, [start_node])  # dfs
        # self.search(graph, start_node)  # bfs
        self.search(graph, start_node, n)  # optimized bfs

        return self.result

# leetcode submit region end(Prohibit modification and deletion)
