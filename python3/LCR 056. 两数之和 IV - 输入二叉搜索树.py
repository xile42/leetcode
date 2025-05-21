# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:

        s = set()
        success = False

        def f(node):

            nonlocal success
            if success or node is None:
                return

            v = node.val
            if k - v in s:
                success = True
                return
            s.add(v)

            f(node.left)
            f(node.right)

        f(root)

        return success
