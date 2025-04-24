class Solution:

    max_depth = None
    sum_value = None

    def search(self, node, depth):

        if node.left is None and node.right is None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.sum_value = node.val
            elif depth == self.max_depth:
                self.sum_value += node.val
            return

        if node.left:
            self.search(node.left, depth+1)
        if node.right:
            self.search(node.right, depth+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0
        self.sum_value = 0

        self.search(root, 1)

        return self.sum_value

