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
        if not node:
            return None

        curr = {node: Node(node.val)}
        queue = [node]

        while queue:
            n = queue.pop(0)

            for value in n.neighbors:
                if value not in curr:
                    curr[value] = Node(value.val)
                    queue.append(value)

                curr[n].neighbors.append(curr[value])

        return curr[node]
