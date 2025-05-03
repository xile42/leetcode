# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        success = True

        def f(p, q):

            nonlocal success

            if not success:
                return

            if p is None and q is None:
                return
            elif p is None or q is None or p.val != q.val:
                success = False
                return

            f(p.left, q.left)
            f(p.right, q.right)

        f(p, q)

        return success