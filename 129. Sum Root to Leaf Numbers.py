# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = [(root, root.val)]

        while queue:
            temp = []

            for node, val in queue:
                if not node.left and not node.right:
                    total += val
                
                if node.left:
                    temp.append((node.left, val * 10 + node.left.val))
                if node.right:
                    temp.append((node.right, val * 10 + node.right.val))
            queue = temp

        return total
