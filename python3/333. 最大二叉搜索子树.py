class Solution:

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if self.isValidBST(root, -inf, inf):
            return self.countNodes(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def isValidBST(self, root: TreeNode, l: int, r: int) -> bool:

        if not root:
            return True
        if root.val <= l or root.val >= r:
            return False

        return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, r)

    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
