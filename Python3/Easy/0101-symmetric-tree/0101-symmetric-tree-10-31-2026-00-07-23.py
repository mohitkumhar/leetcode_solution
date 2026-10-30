# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def solve(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False

            return (
                (leftNode.val == rightNode.val)
                and solve(leftNode.left, rightNode.right)
                and solve(leftNode.right, rightNode.left)
            )

        return solve(root.left, root.right)
