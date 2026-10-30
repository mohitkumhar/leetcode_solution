# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def solve(node):
            if not node:
                val.append(None)
                return None

            solve(node.left)
            solve(node.right)
            val.append(node.val)

        val = []
        solve(p)
        a = val

        val = []
        solve(q)
        b = val

        return a == b
