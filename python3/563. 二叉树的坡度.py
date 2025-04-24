# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node):

            nonlocal ans
            if node is None:
                return 0

            left_value = f(node.left)
            right_value = f(node.right)

            cur_value = abs(left_value - right_value)
            ans += cur_value

            return left_value + right_value + node.val

        f(root)

        return ans
            
