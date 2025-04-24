class Solution:

    result = None

    def search(self, node):

        if node.left is None and node.right is None:
            self.result += 1
            return node.val, 1

        left_value, left_cnt = (0, 0) if node.left is None else self.search(node.left)
        right_value, right_cnt = (0, 0) if node.right is None else self.search(node.right)

        avg_value = (node.val + left_value + right_value) // (left_cnt + right_cnt + 1)
        if avg_value == node.val:
            self.result += 1

        return node.val + left_value + right_value, left_cnt + right_cnt + 1

    def averageOfSubtree(self, root: TreeNode) -> int:

        self.result = 0
        self.search(root)

        return self.result

