# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return False

            if f(node.left):
                node.left = None
            if f(node.right):
                node.right = None
            if node.left is None and node.right is None and node.val == target:
                return True

            return False

        return None if f(root) else root
