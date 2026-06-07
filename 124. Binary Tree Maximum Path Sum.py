# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def post(node):
            if not node:
                return 0

            left_sum = max(0, post(node.left))
            right_sum = max(0, post(node.right))


            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)

            if not node.right and not node.left:
                return node.val
            
            return node.val + max(left_sum, right_sum)
            

        post(root)

        return self.max_sum
