# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
#  A valid BST is defined as follows:
#
#
#  The left subtree of a node contains only nodes with keys less than the
# node's key.
#  The right subtree of a node contains only nodes with keys greater than the
# node's key.
#  Both the left and right subtrees must also be binary search trees.
#
#
#
#  Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 10⁴].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 1695
# 8 👎 1384


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    success = None

    def check(self, node):

        if not self.success:
            return None, None

        min_value, max_value = float("inf"), -float("inf")
        root_value = node.val
        min_value = min(min_value, root_value)
        max_value = max(max_value, root_value)

        if node.left:
            left_min, left_max = self.check(node.left)
            if not self.success:
                return None, None
            if left_max >= root_value:
                self.success = False
            min_value = left_min

        if node.right:
            right_min, right_max = self.check(node.right)
            if not self.success:
                return None, None
            if right_min <= root_value:
                self.success = False
            max_value = right_max

        return min_value, max_value

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.success = True
        self.check(root)

        return self.success

# leetcode submit region end(Prohibit modification and deletion)
