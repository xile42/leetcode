# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    results = None


    def dfs(self, node, path):

        if node.left is None and node.right is None:
            self.results.append(path+[str(node.val)])
            return

        if node.left:
            self.dfs(node.left, path+[str(node.val)])
        if node.right:
            self.dfs(node.right, path+[str(node.val)])


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.results = list()
        self.dfs(root, list())

        return ["->".join(i) for i in self.results]
