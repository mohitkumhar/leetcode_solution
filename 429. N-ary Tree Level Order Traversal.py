"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            temp_nodes = []
            level_val = []

            for node in queue:
                level_val.append(node.val)
                temp_nodes.extend(node.children)

            result.append(level_val)
            queue = temp_nodes

        return result
