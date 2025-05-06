# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = [root]

        while queue:
            temp_nodes =[]

            for node in queue:
                if node.left:
                    if not node.left.left and not node.left.right:
                        total += node.left.val
                    temp_nodes.append(node.left)

                if node.right:
                    temp_nodes.append(node.right)

            queue = temp_nodes

        return total
