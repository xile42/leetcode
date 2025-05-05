# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        ans = list()

        def f(node):

            nonlocal ans

            if node is None:
                return 0

            ans.append(f(node.left))
            f(node.right)

            if node.left is None and node.right is None:
                return node.val
            else:
                return 0

        f(root)

        return sum(ans)