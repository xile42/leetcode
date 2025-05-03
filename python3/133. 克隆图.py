"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        d = dict()
        vis = set()
        adj = defaultdict(list)

        def f(cur):

            if cur is None:
                return None

            vis.add(cur.val)
            for neighbor in cur.neighbors:
                adj[cur.val].append(neighbor.val)
                if neighbor.val in vis:
                    continue
                f(neighbor)

        f(node)

        for v in vis:
            d[v] = Node(val=v)

        for vi, vjs in adj.items():
            for vj in vjs:
                d[vi].neighbors.append(d[vj])

        return d[node.val] if node is not None else None
