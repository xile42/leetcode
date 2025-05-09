# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def f(node, v):

            if node is None:
                return

            node.pval = v + node.val
            f(node.left, node.pval)
            f(node.right, node.pval)

        f(root, 0)

        def ff(node):

            if node is None:
                return -inf, False

            if node.left is None and node.right is None:
                if node.pval < limit:
                    return node.val, True
                else:
                    return node.val, False

            left_value, left_flag = ff(node.left)
            right_value, right_flag = ff(node.right)
            if left_flag:
                node.left = None
            if right_flag:
                node.right = None

            flag = False
            if node.pval + left_value < limit and node.pval + right_value < limit:
                flag = True

            return max(left_value, right_value) + node.val, flag

        dummy = TreeNode(val=inf, left=root)
        dummy.pval = 0
        ff(dummy)

        return dummy.left
