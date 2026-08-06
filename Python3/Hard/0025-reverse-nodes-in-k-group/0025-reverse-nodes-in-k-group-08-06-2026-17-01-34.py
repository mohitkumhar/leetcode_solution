# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k <= 1:
            return head

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

        prevTail = dummy
        first = head
        second = head

        while first:
            count = 1
            second = first

            while count < k and second:
                count += 1
                second = second.next

            if not second:
                break

            newHead, newTail = reverse(first, second)

            prevTail.next = newHead
            prevTail = newTail

            first = newTail.next

        return dummy.next
