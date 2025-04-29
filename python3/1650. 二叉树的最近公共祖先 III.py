"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        ps = set()
        ps.add(p.val)
        while p.parent:
            ps.add(p.parent.val)
            p = p.parent
        if q.val in ps:
            return q
        while q.parent:
            q = q.parent
            if q.val in ps:
                return q
