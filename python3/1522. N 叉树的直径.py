"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        ans = 0

        def f(node):

            nonlocal ans
            if node is None:
                return 0
            if not node.children:
                return 1

            ls = [f(child) for child in node.children]
            ls.sort()
            if ls:
                ans = max(ans, ls[-1])
            if len(ls) >= 2:
                ans = max(ans, sum(ls[-2:]))

            return max(ls) + 1

        f(root)

        return ans
