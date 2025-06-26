# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, path_sum):
            if not node:
                return None

            path_sum += node.val
            if not node.right and not node.left:
                return node if path_sum >= limit else None

            node.left = dfs(node.left, path_sum)
            node.right = dfs(node.right, path_sum)

            if not node.right and not node.left:
                return None
            return node

        return dfs(root, 0)
