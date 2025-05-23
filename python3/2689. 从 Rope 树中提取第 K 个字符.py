# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """

        def f(node):

            if node is None:
                return ""

            if node.left is None and node.right is None:
                return node.val

            return f(node.left) + f(node.right)

        return f(root)[k - 1]
