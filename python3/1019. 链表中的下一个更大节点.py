# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        ans = defaultdict(int)
        cnt = 0
        st = list()
        cur = head
        while cur:
            cnt += 1
            v = cur.val
            while st and st[-1][-1] < v:
                ccnt, vv = st.pop(-1)
                ans[ccnt] = v
            st.append([cnt, v])
            cur = cur.next

        return [ans[i] for i in range(1, cnt + 1)]
