'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        if not head or k == 0:
            return head

        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        k %= length
        
        if k == 0:
            return head

        current = head

        node = Node(0)
        temp_node = node
        
        while k != 0 and current:
            temp_node.next = current
            current = current.next
            temp_node = temp_node.next

            k -= 1

        temp_node.next = None
        
        new_head = current

        while current and current.next:
            current = current.next
        
        current.next = node.next
        
        return new_head
