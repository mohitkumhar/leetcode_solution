# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def height(node):
            nonlocal diameter
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        height(root)

        return diameter
