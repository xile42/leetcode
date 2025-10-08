# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = list()
        queue.append(root)
        cur = 1
        while queue:
            next_queue = list()

            vs = [node.val for node in queue]
            if cur == 1:
                if not all(vs[i] - vs[i - 1] > 0 for i in range(1, len(vs))):
                    return False
            else:
                if not all(vs[i] - vs[i - 1] < 0 for i in range(1, len(vs))):
                    return False

            for node in queue:
                if node.val % 2 != cur:
                    return False
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue
            cur = 1 - cur

        return True
