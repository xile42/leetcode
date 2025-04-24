class Solution:

    node_value = None
    prefix_sum = None

    def search(self, node):

        if node is None:
            return 0

        self.search(node.left)
        self.search(node.right)
        self.node_value.append(node.val)

    def update(self, node):

        if node is None:
            return

        node.val = node.val + self.prefix_sum[node.val]
        self.update(node.left)
        self.update(node.right)

    def convertBST(self, root: TreeNode) -> TreeNode:

        self.node_value = list()
        self.search(root)
        self.node_value = sorted(self.node_value, reverse=True)
        self.prefix_sum = dict()
        sum_value = 0
        for idx, num in enumerate(self.node_value):
            sum_value += 0 if idx == 0 else self.node_value[idx-1]
            self.prefix_sum[num] = sum_value

        self.update(root)

        return root
