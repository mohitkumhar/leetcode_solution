'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        if not head:
            return Node(x)

        current = head
        
        while current.next is not None:
            current = current.next
        
        node = Node(x)
        
        current.next = node
        
        return head
