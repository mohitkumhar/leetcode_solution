'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def flattenBST(self, root):
        
        def solve(node):
            if not node:
                return None
        
            left_head = solve(node.left)
            right_head = solve(node.right)
            
            node.left = None
            
            if left_head:
                head = left_head
                
                while head and head.right:
                    head = head.right
                
                head.right = node
                node.right = right_head
            
                return left_head
            
            else:
                head = node
                head.right = right_head
                
                return node

        return solve(root)
