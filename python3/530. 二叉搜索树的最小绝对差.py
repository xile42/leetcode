# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        ns = list()

        def f(node):

            if node is None:
                return

            f(node.left)
            ns.append(node.val)
            f(node.right)

        f(root)

        return min(ns[i] - ns[i - 1] for i in range(1, len(ns)))
