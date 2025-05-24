# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node or p == node or q == node:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                return node
            return left if left else right
        
        return dfs(root, p, q)
