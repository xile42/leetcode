# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):

        nodes = list()

        def f(node):

            if node is None:
                return

            nonlocal nodes
            f(node.left)
            nodes.append(node.val)
            f(node.right)

        f(root)
        self.nodes = nodes
        self.cur = None

    def next(self) -> int:

        self.cur = 0 if self.cur is None else self.cur + 1

        return self.nodes[self.cur]

    def hasNext(self) -> bool:

        return True if self.cur is None or self.cur < len(self.nodes) - 1 else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()