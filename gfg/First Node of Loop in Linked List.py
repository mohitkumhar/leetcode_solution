"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        seen = set()
        current = head

        while current:
            if current in seen:
                return current.data

            seen.add(current)
            current=current.next

        return -1
