# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return None

            if node.val % 2 == 0:
                if node.left and node.left.left:
                    self.ans += node.left.left.val
                if node.left and node.left.right:
                    self.ans += node.left.right.val

                if node.right and node.right.left:
                    self.ans += node.right.left.val
                if node.right and node.right.right:
                    self.ans += node.right.right.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.ans
