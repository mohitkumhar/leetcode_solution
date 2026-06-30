'''
Definition for Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        self.ans = float('-inf')
        
        def solve(node):
            if not node:
                return 0

            left_height = max(0, solve(node.left))
            right_height = max(0, solve(node.right))
            
            self.ans = max(self.ans, left_height + right_height + node.data)
            
            return node.data + max(left_height, right_height)
        
        solve(root)
        
        return self.ans
