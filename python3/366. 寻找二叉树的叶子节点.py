# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def f(node):

            if node is None:
                return [], False

            if node.left is None and node.right is None:
                return [node.val], True

            left, left_is_leaf = f(node.left)
            right, right_is_leaf = f(node.right)
            if left_is_leaf:
                node.left = None
            if right_is_leaf:
                node.right = None

            return left + right, False

        ans = list()
        while root:
            leaf, is_leaf = f(root)
            ans.append(leaf)
            if is_leaf:
                break

        return ans

