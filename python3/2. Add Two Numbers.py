# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result_head = ListNode()
        result_current = result_head
        carry = 0
        carry_flag = False
        l1_current = l1
        l2_current = l2

        while True:

            this_value = 0
            if l1_current is None and l2_current is None:
                if carry == 1:
                    this_value = 1
                else:
                    break
            elif l1_current is None:
                this_value = l2_current.val + carry
            elif l2_current is None:
                this_value = l1_current.val + carry
            else:
                this_value = l1_current.val + l2_current.val + carry

            if this_value >= 10:
                carry_flag = True
                this_value %= 10

            this_node = ListNode()
            this_node.val = this_value
            result_current.next = this_node
            result_current = result_current.next
            carry = 0 if not carry_flag else 1
            carry_flag = False

            if l1_current is not None:
                l1_current = l1_current.next
            if l2_current is not None:
                l2_current = l2_current.next

        return result_head.next
