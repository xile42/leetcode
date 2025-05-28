# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        vs = list()

        def f(node, val):
            nonlocal vs
            if node is None:
                return

            node.val = val
            vs.append(val)
            f(node.left, 2 * val + 1)
            f(node.right, 2 * val + 2)

        f(root, 0)
        self.vs = set(vs)

    def find(self, target: int) -> bool:
        return target in self.vs

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)