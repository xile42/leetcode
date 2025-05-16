# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def f(ns):

            if not ns:
                return None

            i = len(ns) // 2
            v = ns[i]
            root = TreeNode(v)
            root.left = f(ns[:i])
            root.right = f(ns[i + 1:])

            return root

        return f(nums)
