'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isBST(self, root):
        self.inorder = []

        def solve(node):
            if not node:
                return None
            
            solve(node.left)
            self.inorder.append(node.data)
            solve(node.right)
        
        solve(root)
        
        for i in range(1, len(self.inorder)):
            if self.inorder[i] <= self.inorder[i - 1]:
                return False

        return True
