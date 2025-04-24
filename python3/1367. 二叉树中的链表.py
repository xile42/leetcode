# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        tar = str()
        cur = head
        while cur is not None:
            tar += str(cur.val)
            cur = cur.next

        found = False

        def f(node, path):

            nonlocal found
            if found:
                return

            if node is None:
                if tar in path:
                    found = True
                return

            f(node.left, path + str(node.val))
            f(node.right, path + str(node.val))

        f(root, str())

        return found