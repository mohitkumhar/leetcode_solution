"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        count = 0
        queue = [root]

        while queue:
            temp = []
            for node in queue:
                if node.children:
                    temp.extend(node.children)

            count += 1
            queue = temp

        return count