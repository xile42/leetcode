from collections import defaultdict


class Solution:

    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:

        weights = [i[-1] for i in edges]
        # new_edges = defaultdict(dict)
        # for i, j, w in edges:
        #     if j not in new_edges[i]:
        #         new_edges[i][j] = w
        #     else:
        #         new_edges[i][j] = min(new_edges[i][j], w)
        # edges = list()
        # for i in new_edges:
        #     for j in new_edges[i]:
        #         edges.append([i, j, new_edges[i][j]])

        def dfs(g, i, checked):

            vis = set()
            vis.add(i)
            queue = [i]
            while queue:
                node = queue.pop(0)
                for other_node in g[node]:
                    if other_node in vis:
                        continue
                    if other_node == 0 or other_node in checked:
                        return True
                    vis.add(other_node)
                    queue.append(other_node)
            return False

        def check(k):

            g = defaultdict(list)
            for i, j, w in edges:
                if w > k:
                    continue
                g[i].append(j)
                # if len(g[i]) > threshold:
                #     print("checking k, {} nodes > threshold".format(i), g[i])
                #     return False

            checked = set()
            for node in range(1, n):
                if not dfs(g, node, checked):
                    # print("checking k, {} can not reach 0".format(node))
                    return False
                else:
                    checked.add(node)

            return True

        left, right = min(weights), max(weights)
        # print(left, right)
        while left <= right:
            mid = left + (right - left) // 2
            # print("checking", mid, check(mid))
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return -1 if left > max(weights) else left
