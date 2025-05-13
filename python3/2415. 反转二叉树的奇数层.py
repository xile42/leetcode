# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node, other_node, is_odd):

            if node is None:
                return

            if is_odd:
                node.val, other_node.val = other_node.val, node.val
            f(node.left, other_node.right, not is_odd)
            f(node.right, other_node.left, not is_odd)

        f(root.left, root.right, True)

        return root
