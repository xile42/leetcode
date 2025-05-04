# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:

        def f(node):

            if node is None:
                return "()"

            s = str(node.val)
            if node.left and node.right:
                s += "({})({})".format(f(node.left), f(node.right))
            elif node.left:
                s += "({})".format(f(node.left))
            elif node.right:
                s += "()({})".format(f(node.right))

            return s

        ans = f(root)

        return ans
