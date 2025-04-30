# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        vs = set([node.val for node in nodes])
        n = len(vs)
        ans = None

        def f(node):

            if node is None:
                return 0

            nonlocal ans
            if ans is not None:
                return 0

            left = f(node.left)
            right = f(node.right)
            v = left + right + (1 if node.val in vs else 0)
            if v == n:
                ans = node
                return 0

            return v

        f(root)

        return ans
