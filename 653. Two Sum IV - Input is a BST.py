# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []
        def dfs(node):
            if not node:
                return None
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        seen = set()
        for num in result:
            if k - num in seen:
                return True
            seen.add(num)

        return False
