# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathTarget(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = list()

        def f(node, path, cur):

            nonlocal ans
            if node is None:
                return

            if node.left is None and node.right is None:
                if cur + node.val == targetSum:
                    ans.append(path + [node.val])
                return

            if node.left:
                f(node.left, path + [node.val], cur + node.val)
            if node.right:
                f(node.right, path + [node.val], cur + node.val)

        f(root, [], 0)

        return ans
