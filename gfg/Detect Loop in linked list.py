'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        current = head
        seen = set()

        while current and current.next:
            if current in seen:
                return True
            
            seen.add(current)
            current = current.next

        return False
