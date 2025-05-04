# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return None

            node.left = f(node.left)
            node.right = f(node.right)

            return (node.left or node.right) if not (low <= node.val <= high) else node

        return f(root)
