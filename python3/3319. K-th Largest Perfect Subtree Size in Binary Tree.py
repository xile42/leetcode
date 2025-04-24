# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    results = None

    def search(self, node):

        if node.left is None and node.right is None:
            self.results.append(1)
            return True, 1

        if not (node.left is not None and node.right is not None):
            if node.left:
                self.search(node.left)
            if node.right:
                self.search(node.right)
            return False, -1

        left_check, left_depth = self.search(node.left)
        right_check, right_depth = self.search(node.right)
        if not (left_check and right_check):
            return False, -1
        if left_depth != right_depth:
            return False, -1

        self.results.append(1 + 2 * (pow(2, left_depth) - 1))
        return True, left_depth + 1

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        self.results = list()
        self.search(root)
        self.results = sorted(self.results, reverse=True)

        return -1 if k - 1 >= len(self.results) else self.results[k-1]
