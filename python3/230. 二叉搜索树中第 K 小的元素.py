# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        vals = list()

        def dfs(node):

            if node is None:
                return

            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return sorted(vals)[k - 1]
