# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if head is None:
            return [-1, -1]

        pos = list()
        idx = 0
        pre = head
        cur = head.next
        while cur and cur.next:
            if pre.val < cur.val and cur.next.val < cur.val:
                pos.append(idx)
            elif pre.val > cur.val and cur.next.val > cur.val:
                pos.append(idx)
            idx += 1
            pre = cur
            cur = cur.next

        if not pos or len(pos) < 2:
            return [-1, -1] 
        
        diffs = [pos[i] - pos[i - 1] for i in range(1, len(pos))]

        return [min(diffs), pos[-1] - pos[0]]
            

