"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:

    def toArray(self, root: 'Optional[Node]') -> List[int]:

        ans = list()
        cur = root
        while cur:
            ans.append(cur.val)
            cur = cur.next

        return ans
