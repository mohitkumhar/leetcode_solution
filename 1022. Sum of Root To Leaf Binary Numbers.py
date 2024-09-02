# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if node is None:
                return None
            
            path += str(node.val)

            if node.left is None and node.right is None:
                return int(path, 2)
            
            left_sum = dfs(node.left, path)
            right_sum = dfs(node.right, path)
        
            return (left_sum if left_sum else 0) + (right_sum if right_sum else 0)

        return dfs(root, "")
            
        
        