# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def dfs(node, parent, depth, val):
            if not node:
                return None
            
            elif node.val is val:
                return (parent, depth)
            
            return dfs(node.left, node, depth + 1, val) or dfs(node.right, node, depth + 1, val)
        

        px, dx = dfs(root, None, 0, x)
        py, dy = dfs(root, None, 0, y)
        
        return px != py and dx == dy