"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        current = head

        while current:
            if current.child:

                child_head = current.child
                child_tail = child_head

                while child_tail.next:
                    child_tail = child_tail.next
                
                child_tail.next = current.next
                
                if current.next:
                    current.next.prev = child_tail

                current.next = child_head
                child_head.prev = current
                
                current.child = None
            
            current = current.next
        
        return head
        
        