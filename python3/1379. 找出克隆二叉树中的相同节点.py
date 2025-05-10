# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def f(node):

            if node is None:
                return None

            if node.val == target.val:
                return node

            return f(node.left) or f(node.right)

        return f(cloned)
