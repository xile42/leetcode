class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode()
        result = dummy_head
        slow = head
        fast = head.next

        while True:

            node_sum = 0
            while fast is not None and fast.val != 0:
                node_sum += fast.val
                fast = fast.next
            if fast is None:
                break
            node = ListNode(val=node_sum)
            result.next = node
            result = result.next

            slow = fast
            fast = fast.next

        return dummy_head.next
