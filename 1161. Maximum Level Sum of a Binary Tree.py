# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        level = 1
        max_sum = -float('inf')
        min_level = 0

        while queue:
            temp = []
            level_order = []

            for node in queue:
                level_order.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            prev_max_sum = max_sum
            temp_sum = sum(level_order)
            max_sum = max(max_sum, temp_sum)
            
            if temp_sum > prev_max_sum:
                min_level = level
            
            level += 1
            queue = temp

        return min_level


