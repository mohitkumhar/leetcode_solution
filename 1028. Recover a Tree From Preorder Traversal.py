# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        self.i = 0
        n = len(traversal)

        def solve(s, depth):
            j = self.i
            dash = 0

            while j < n and s[j] == '-':
                dash += 1
                j += 1
            
            if dash != depth:
                return None
            
            self.i = j

            num = 0
            while self.i < n and s[self.i].isdigit():
                num = (num * 10) + int(s[self.i])
                self.i += 1
            
            node = TreeNode(num)

            node.left = solve(s, depth + 1)
            node.right = solve(s, depth + 1)

            return node

            
        return solve(traversal, 0)
        



