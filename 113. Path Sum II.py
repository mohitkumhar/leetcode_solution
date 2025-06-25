# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, curr_sum):
            if not node:
                return None

            path.append(node.val)
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(list(path))

            node.left = dfs(node.left, path, curr_sum)
            node.right = dfs(node.right, path, curr_sum)
            path.pop()

        result = []
        dfs(root, [], 0)
        return result
