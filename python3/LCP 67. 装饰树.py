# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return None

            if node.left:
                new = TreeNode(val=-1)
                new.left = f(node.left)
                node.left = new

            if node.right:
                new = TreeNode(val=-1)
                new.right = f(node.right)
                node.right = new

            return node

        f(root)

        return root
