# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        ans = list()

        def f(node, single):

            nonlocal ans

            if node is None:
                return

            if single:
                ans.append(node.val)

            if node.left is None and node.right:
                f(node.right, True)
            elif node.left and node.right is None:
                f(node.left, True)
            else:
                f(node.left, False)
                f(node.right, False)

        f(root, False)

        return ans
