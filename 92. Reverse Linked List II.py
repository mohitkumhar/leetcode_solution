# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        start = prev.next
        then = start.next

        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            
            prev.next = then

            then = start.next
        
        return dummy.next
