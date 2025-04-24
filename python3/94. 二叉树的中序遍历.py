# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def search(self, node):

        if node is None:
            return list()

        return self.search(node.left) + [node.val] + self.search(node.right)
        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        return self.search(root)      
