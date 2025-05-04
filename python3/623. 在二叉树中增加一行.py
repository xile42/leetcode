# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def f(node, cur):

            if node is None:
                return

            if cur == depth - 1:
                left = TreeNode(val)
                right = TreeNode(val)
                left.left = node.left
                right.right = node.right
                node.left = left
                node.right = right
                return

            f(node.left, cur + 1)
            f(node.right, cur + 1)

        f(root, 1)

        return root
