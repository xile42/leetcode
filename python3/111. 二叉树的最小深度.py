# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:

        def f(node):

            if node is None:
                return inf

            if node.left is None and node.right is None:
                return 1

            return min(f(node.left), f(node.right)) + 1

        return ans if (ans := f(root)) < inf else 0
