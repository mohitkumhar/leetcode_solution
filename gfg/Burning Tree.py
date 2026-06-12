'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        matrix = {}  # u: v; v: u
        stack = [root]

        while stack:
            node = stack.pop()
            
            if node.data not in matrix:
                matrix[node.data] = []
            
            if node.left:
                stack.append(node.left)
                
                matrix[node.data].append(node.left.data)
                if node.left.data not in matrix:
                    matrix[node.left.data] = []
                matrix[node.left.data].append(node.data)

            if node.right:
                stack.append(node.right)
                
                matrix[node.data].append(node.right.data)
                if node.right.data not in matrix:
                    matrix[node.right.data] = []
                matrix[node.right.data].append(node.data)
            
        queue = [target]
        count = -1
        seen = {target}
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                node = queue.pop(0)
                
                for nei in matrix[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            
            count += 1
        
        return count

