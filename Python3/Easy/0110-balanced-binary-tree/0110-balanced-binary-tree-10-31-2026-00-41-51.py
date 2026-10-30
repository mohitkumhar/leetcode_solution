# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def solve(node):
            if not node:
                return 0

            leftHeight = solve(node.left)
            if leftHeight == -1:
                return -1

            rightHeight = solve(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        if solve(root) == -1:
            return False
        return True
