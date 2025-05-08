# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return False

            cur = node.val == 1

            left = f(node.left)
            right = f(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None

            return cur or left or right

        return None if not f(root) else root
