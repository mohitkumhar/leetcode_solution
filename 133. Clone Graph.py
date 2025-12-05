"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        
        clone = {node: Node(node.val)}

        queue = [node]

        while queue:
            current = queue.pop(0)

            for values in current.neighbors:
                if values not in clone:
                    clone[values] = Node(values.val)
                    queue.append(values)
                
                clone[current].neighbors.append(clone[values])
        
        return clone[node]


