# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.total_sum = 0
        MOD = 10**9 + 7

        def total_sum(node):
            if not node:
                return 0
            total_sum(node.left)
            total_sum(node.right)
            self.total_sum += node.val

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            sub_tree_sum = left_sum + right_sum + node.val
            curr_max = (self.total_sum - sub_tree_sum) * sub_tree_sum

            self.result = max(self.result, curr_max)

            return sub_tree_sum

        total_sum(root)
        dfs(root)

        return self.result % MOD
