"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        leftMost = root

        while leftMost:

            level_head = None
            prev = None

            node = leftMost

            while node:
                
                if node.left:
                    
                    if not level_head:
                        level_head = node.left
                    
                    if prev:
                        prev.next = node.left
                
                    prev = node.left
                
                if node.right:

                    if not level_head:
                        level_head = node.right

                    if prev:
                        prev.next = node.right
                    
                    prev = node.right
                
                node = node.next
            
            leftMost = level_head
        
        return root
