"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        current = head

        dummy = Node(0)
        node = dummy

        while current:
            node.next = Node(current.val)

            node = node.next
            current = current.next
        
        node = dummy.next
        current = head

        while current:

            if current.random:

                head_temp = head
                dummy_temp = dummy.next

                while head_temp:
                    if head_temp == current.random:
                        break
                    head_temp = head_temp.next
                    dummy_temp = dummy_temp.next
                
                node.random = dummy_temp
            
            current = current.next
            node = node.next
        
        return dummy.next
