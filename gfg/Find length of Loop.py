'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        
        seen = {}
        
        current = head
        j = 0
        
        while current and current.next:
            if current in seen:
                length = j - seen[current]
                return length

            seen[current] = j
            current = current.next
            j += 1


        return 0
