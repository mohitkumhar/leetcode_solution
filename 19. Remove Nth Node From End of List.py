# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def size():
            current = head
            size = 0
            while current != None:
                size += 1
                current = current.next

            return size

        position = 1

        size = size()
        current = head

        while current.next and position != size - n:
            current = current.next
            position += 1

        if size == 1 and n == 1:
            head = None
            return head

        # condition of first node removing
        if size - n == 0:
            head = head.next

        # condition of removing last Node
        elif current.next.next == None:
            current.next = None

        # condition of removing middle node
        elif current.next.next != None:
            current.next = current.next.next

        return head
