# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def f(node):

            if node is None:
                return list()

            return f(node.left) + f(node.right) + [node.val]

        return f(root)

