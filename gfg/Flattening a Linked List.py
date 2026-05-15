'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        
        def merge(a, b):
            if not a:
                return b
            if not b:
                return a
            
            dummy = Node(0)
            temp = dummy
            
            while a and b:
                if a.data < b.data:
                    temp.bottom = a
                    a = a.bottom
                
                else:
                    temp.bottom = b
                    b = b.bottom
                
                temp = temp.bottom
                temp.next = None

            if a:
                temp.bottom = a
            if b:
                temp.bottom = b
            
            return dummy.bottom


        def solve(node):
            if not node:
                return None

            head1 = node
            head2 = solve(node.next)

            node = merge(head1, head2)

            return node
        
        return solve(root)
        
