# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def f(ns):

            if not ns:
                return None

            root_val = ns[0]
            i = 1
            while i < len(ns) and ns[i] < root_val:
                i += 1

            node = TreeNode(val=root_val, left=f(ns[1:i]), right=f(ns[i:]))

            return node

        return f(preorder)
