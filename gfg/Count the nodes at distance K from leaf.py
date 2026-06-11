'''
 class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def kthFromLeaf(self, root, k):
        seen = set()
        self.count = 0

        def solve(node, curr_path):
            if not node:
                return 0
            
            curr_path.append(node)
            
            if not node.left and not node.right:
                if len(curr_path) > k:
                    val = curr_path[-(k + 1)]

                    if val not in seen:
                        seen.add(val)
                        self.count += 1
        
            solve(node.left, curr_path)
            solve(node.right, curr_path)
            
            curr_path.pop()
        
        solve(root, [])
        
        return self.count
