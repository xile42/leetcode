class Solution:

    def generate(self, nums):

        if len(nums) == 0:
            return None

        max_value = max(nums)
        max_idx = nums.index(max_value)

        node = TreeNode(val=max_value)
        left_node = self.generate(nums[:max_idx])
        right_node = self.generate(nums[max_idx+1:])

        node.left = left_node
        node.right = right_node

        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        node = self.generate(nums)

        return node
