class Solution:

    values = None

    def search(self, node):

        if node is None:
            return

        self.values.append(node.val)
        self.search(node.left)
        self.search(node.right)

    def generate(self, nums):

        if len(nums) == 0:
            return None

        mid_idx = len(nums) // 2
        mid_value = nums[mid_idx]
        node = TreeNode(val=mid_value)
        left_node = self.generate(nums[:mid_idx])
        right_node = self.generate(nums[mid_idx+1:])
        node.left = left_node
        node.right = right_node

        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.values = list()
        self.search(root)
        node = self.generate(sorted(self.values))

        return node
