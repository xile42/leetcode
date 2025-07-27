# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        pre = None
        ans = None

        def f(node):

            if node is None:
                return

            f(node.left)
            nonlocal pre, ans
            if pre == p:
                ans = node
            pre = node
            f(node.right)

        f(root)

        return ans
