# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def solve(node):
            if not node or node == p or node == q:
                return node

            left = solve(node.left)
            right = solve(node.right)

            if left and right:
                return node

            return left or right

        return solve(root)
