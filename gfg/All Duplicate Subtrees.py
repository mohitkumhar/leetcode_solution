''' Structure of a Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def printAllDups(self, root):
        seen = {}
        self.result = []
        
        def solve(node):
            if not node:
                return "#"

            left = solve(node.left)
            right = solve(node.right)
        
            curr_tree = f"{node.data}, {left}, {right}"
            
            if curr_tree not in seen:
                seen[curr_tree] = 0
            seen[curr_tree] += 1
            
            if seen[curr_tree] == 2:
                self.result.append(node)
            
            return curr_tree
            
        solve(root)
        
        return self.result
            



