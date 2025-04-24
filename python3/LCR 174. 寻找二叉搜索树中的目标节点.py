# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:

        ns = list()

        def f(node):

            nonlocal ns
            if node is None:
                return

            ns.append(node.val)
            f(node.left)
            f(node.right)

        f(root)

        return sorted(ns)[-cnt]
