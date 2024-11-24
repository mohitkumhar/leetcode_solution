# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """


        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        current = slow.next

        slow.next = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        