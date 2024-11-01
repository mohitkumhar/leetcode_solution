# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        
        # find length
        current = head
        length = 0
        while current:
            current = current.next
            length += 1

        k = k % length

        if k == 0:
            return head
        

        fast = slow = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
    
        return new_head
