# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(first, second):
            stop = second.next
            prev = stop
            curr = first

            while curr != stop:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return second, first

        dummy = ListNode(0)
        dummy.next = head

        prevGrpTail = dummy
        first = head
        second = head

        while first:

            second = first
            count = 1

            while count < k and second:
                count += 1
                second = second.next

            if not second:
                break

            newHead, newTail = reverse(first, second)

            prevGrpTail.next = newHead
            prevGrpTail = newTail

            first = newTail.next

        return dummy.next
