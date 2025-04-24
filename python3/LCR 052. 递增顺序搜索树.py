# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):

            if node is None:
                return []

            return dfs(node.left) + [node] + dfs(node.right)

        nodes = dfs(root)
        head = TreeNode()
        cur = head
        for node in nodes:
            node.left = None
            node.right = None
            cur.right = node
            cur = cur.right

        return head.right
