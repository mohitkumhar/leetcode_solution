# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]

        while queue:
            temp_node = []

            for node in queue:

                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            
            if not temp_node:
                return queue[0].val

            queue = temp_node
