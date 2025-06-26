class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def f(node):

            nonlocal last, first
            if node:
                f(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                f(node.right)

        if not root:
            return None

        first, last = None, None
        f(root)

        last.right = first
        first.left = last

        return first
