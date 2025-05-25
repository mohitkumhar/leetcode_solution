# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        queue = [root]

        while queue:
            temp = []
            for node in queue:
                result.append(node.val)
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        
        result.sort()
        min_diff = float('inf')

        for i in range(1, len(result)):
            diff = abs(result[i - 1] - result[i])
            min_diff = min(min_diff, diff)
        
        return min_diff
