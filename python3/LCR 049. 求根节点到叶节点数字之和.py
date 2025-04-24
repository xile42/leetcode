# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    results = None

    def search(self, node, used):

        if node.left is None and node.right is None:
            self.results.append(int(used+str(node.val)))
            return

        if node.left:
            self.search(node.left, used+str(node.val))

        if node.right:
            self.search(node.right, used+str(node.val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.results = list()
        self.search(root, str())

        return sum(self.results)
