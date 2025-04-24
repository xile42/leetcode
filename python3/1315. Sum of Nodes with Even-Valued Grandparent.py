class Solution:

    result = None

    def search(self, node, grandparent, parent):

        if grandparent is not None and grandparent.val % 2 == 0:
            self.result += node.val

        if node.left:
            self.search(node.left, parent, node)

        if node.right:
            self.search(node.right, parent, node)

    def sumEvenGrandparent(self, root: TreeNode) -> int:

        self.result = 0
        self.search(root, None, None)

        return self.result
