# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2

        carry = 0

        dummy = ListNode(0)
        curr = dummy

        while curr1 != None or curr2 != None or carry:

            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            currVal = val1 + val2 + carry

            carry = currVal // 10
            digit = currVal % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        result = dummy.next

        return result
