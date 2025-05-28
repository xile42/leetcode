# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        ns = list()

        def f(node):

            if node is None:
                return

            ns.append(node.val)
            f(node.left)
            f(node.right)

        f(root1)
        f(root2)

        return sorted(ns)
