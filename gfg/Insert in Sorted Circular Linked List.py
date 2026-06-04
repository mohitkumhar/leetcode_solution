'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   '''     
        
class Solution:
    def sortedInsert(self, head, data):
        node = Node(data)

        # insert before head
        if data < head.data:
            
            current = head
            while current.next != head:
                current = current.next
            
            current.next = node
            node.next = head
            head = node
            return head


            # insert in middle
        
        current = head
        
        while current.next != head:
            if current.data <= data < current.next.data:
                node.next = current.next
                current.next = node
                return head
            current = current.next
            

        # insert in the end
        current.next = node
        node.next = head
        
        return head
