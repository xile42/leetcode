# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        ans = list()
        s = set(to_delete)

        def f(node):

            if node is None:
                return False

            left_flag = f(node.left)
            right_flag = f(node.right)
            if left_flag:
                node.left = None
            if right_flag:
                node.right = None

            if node.val in s:
                if node.left and node.left.val not in s:
                    ans.append(node.left)
                if node.right and node.right.val not in s:
                    ans.append(node.right)

            return node.val in s

        dummy = TreeNode(val=inf, left=root)
        f(dummy)

        if root.val not in s:
            ans.append(root)

        return ans
