''' Structure of linked list Node
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        current = head
        seen = set()
        
        while current and current.next:
            if current.next in seen:
                current.next = None

            seen.add(current)
            current = current.next        
